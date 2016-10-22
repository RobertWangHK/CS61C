// include SSE intrinsics
#if defined(_MSC_VER)
#include <intrin.h>
#elif defined(__GNUC__) && (defined(__x86_64__) || defined(__i386__))
#include <x86intrin.h>
#endif

// include OpenMP
#if !defined(_MSC_VER)
#include <pthread.h>
#endif
#include <omp.h>

#include "calcDepthOptimized.h"
#include "calcDepthNaive.h"

void calcDepthOptimized(float *depth, float *left, float *right, int imageWidth, int imageHeight, int featureWidth, int featureHeight, int maximumDisplacement)
{
	#pragma omp parallel for
	for (int x = 0; x < imageWidth; x++)
	{
		for (int y = 0; y < imageHeight; y++)		
		{
			if ((y < featureHeight) || (y >= imageHeight - featureHeight) || (x < featureWidth) || (x >= imageWidth - featureWidth))
			{
				depth[y * imageWidth + x] = 0;
				continue;
			}

			float minimumSquaredDifference = -1;
			int minimumDy = 0;
			int minimumDx = 0;

			for (int dx = -maximumDisplacement; dx <= maximumDisplacement; dx++)
			{
				if (x + dx - featureWidth < 0 || x + dx + featureWidth >= imageWidth)
				{
					continue;
				}

				for (int dy = -maximumDisplacement; dy <= maximumDisplacement; dy++)
				{
					if (y + dy - featureHeight < 0 || y + dy + featureHeight >= imageHeight)
					{
						continue;
					}

					float squaredDifference = 0;
					__m128 left_reg = _mm_setzero_ps();
					__m128 right_reg = _mm_setzero_ps();
					__m128 diff_reg = _mm_setzero_ps();
					__m128 diff = _mm_setzero_ps();
					float result[4];
					int boxX;

					for (boxX = -featureWidth; boxX < featureWidth / 4 * 4; boxX += 4)
					{
						for (int boxY = -featureHeight; boxY <= featureHeight; boxY++)
						{
							int leftX = x + boxX;
							int leftY = y + boxY;
							int rightX = x + dx + boxX;
							int rightY = y + dy + boxY;

							left_reg = _mm_loadu_ps(left + (leftY * imageWidth + leftX));
							right_reg = _mm_loadu_ps(right + (rightY * imageWidth + rightX)); 
							diff_reg = _mm_sub_ps (left_reg, right_reg);
							diff = _mm_add_ps(diff,_mm_mul_ps(diff_reg, diff_reg));
						}
					}	

					_mm_storeu_ps(result, diff);
					squaredDifference += result[0] + result[1] + result[2] + result[3];

					if ((minimumSquaredDifference != -1) && (minimumSquaredDifference < squaredDifference))
					{
							continue;
					}
					for (int boxY = -featureHeight; boxY <= featureHeight; boxY++) 
					{
						if (featureWidth % 2 == 0)
						{
							int leftX = x + boxX;
							int leftY = y + boxY;
							int rightX = x + dx + boxX;
							int rightY = y + dy + boxY;

							float result = left[leftY * imageWidth + leftX] - right[rightY * imageWidth + rightX];
							squaredDifference += result * result;
						}
						else {

							int leftX = x + boxX;
							int leftY = y + boxY;
							int rightX = x + dx + boxX;
							int rightY = y + dy + boxY;

							left_reg = _mm_loadu_ps(left + (leftY * imageWidth + leftX));
							right_reg = _mm_loadu_ps(right + (rightY * imageWidth + rightX)); 
							diff_reg = _mm_sub_ps (left_reg, right_reg);
							_mm_storeu_ps(result,_mm_mul_ps(diff_reg, diff_reg));
							squaredDifference += result[0] + result[1] + result[2];
						}
					}
					if ((minimumSquaredDifference == -1) || ((minimumSquaredDifference == squaredDifference) && (displacementNaive(dx, dy) < displacementNaive(minimumDx, minimumDy))) || (minimumSquaredDifference > squaredDifference))
					{
						minimumSquaredDifference = squaredDifference;
						minimumDx = dx;
						minimumDy = dy;
					}
				}
			}

			if (minimumSquaredDifference != -1)
			{
				if (maximumDisplacement == 0)
				{
					depth[y * imageWidth + x] = 0;
				}
				else
				{
					depth[y * imageWidth + x] = displacementNaive(minimumDx, minimumDy);
				}
			}
			else
			{
				depth[y * imageWidth + x] = 0;
			}
		}
	}
}