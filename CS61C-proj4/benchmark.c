// CS 61C Fall 2014 Project 3

#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#if defined(_MSC_VER)
#include <intrin.h>
#endif

#include "calcDepthNaive.h"
#include "calcDepthOptimized.h"
#include "utils.h"

#define ARRAY_SIZE(array) (sizeof((array))/sizeof((array[0])))

#if defined(_MSC_VER)
#pragma intrinsic(__rdtsc)
#else

static __inline__ uint64_t __rdtsc()
{
	uint32_t hi, lo;
	__asm__ volatile
		(
		"rdtsc"
		: "=a"(lo), "=d"(hi)
		);
	return (((uint64_t)hi) << 32) | ((uint64_t)lo);
}
#endif

static bool benchmarkMatrix(int imageWidth, int imageHeight, int featureWidth, int featureHeight, int maximumDisplacement)
{
	float* left = (float*)malloc(sizeof(float)* imageWidth * imageHeight);
	if (left == NULL)
	{
		allocationFailed();
	}

	float* right = (float*)malloc(sizeof(float)* imageWidth * imageHeight);
	if (right == NULL)
	{
		free(left);
		allocationFailed();
	}

	fillRandomFloat(left, imageWidth * imageHeight);
	fillRandomFloat(right, imageWidth * imageHeight);

	float* depthNaive = (float*)malloc(sizeof(float)* imageWidth * imageHeight);
	if (depthNaive == NULL)
	{
		free(left);
		free(right);
		allocationFailed();
	}

	float* depthOptimized = (float*)malloc(sizeof(float)* imageWidth * imageHeight);
	if (depthOptimized == NULL)
	{
		free(left);
		free(right);
		free(depthNaive);
		allocationFailed();
	}

	double speedup;
	uint64_t startTSC, endTSC;

	// Get total clock cycles for optimised
	startTSC = __rdtsc();
	calcDepthOptimized(depthOptimized, left, right, imageWidth, imageHeight, featureWidth, featureHeight, maximumDisplacement);
	endTSC = __rdtsc();
	double optimizedTSC = endTSC - startTSC;

	// Get total clock cycles for naive
	startTSC = __rdtsc();
	calcDepthNaive(depthNaive, left, right, imageWidth, imageHeight, featureWidth, featureHeight, maximumDisplacement);
	endTSC = __rdtsc();
	double naiveTSC = endTSC - startTSC;

	// Speedup is just naive / optimised
	speedup = naiveTSC / optimizedTSC;
	printf("%.4f Speedup Ratio\r\n", speedup);

	for (size_t i = 0; i < imageWidth * imageHeight; i++)
	{
		if (!floatsWithinTolerance(depthNaive[i], depthOptimized[i]))
		{
			free(left);
			free(right);
			free(depthNaive);
			free(depthOptimized);
			return false;
		}
	}

	free(left);
	free(right);
	free(depthNaive);
	free(depthOptimized);

	return true;
}

int main(int argc, char** argv)
{
	int returnResult = 0;

	// Fix random seed, please don't precompute things
    srand(0xDEAD + 0x61C + 0xEEC5);

	int tests[][5] = { { 250, 250, 4, 4, 6 }, { 250, 250, 6, 6, 6 }, { 500, 500, 4, 4, 6 }, { 500, 500, 6, 6, 6 }, { 750, 750, 8, 8, 6 } };

	printf("Testing non-odd cases: \r\n");
	for (int i = 0; i < ARRAY_SIZE(tests); i++)
	{
		printf("Testing %ix%i image, feature width %i, feature height %i, maximum diplacement %i... ", tests[i][0], tests[i][1], tests[i][2], tests[i][3], tests[i][4]);
		if (!benchmarkMatrix(tests[i][0], tests[i][1], tests[i][2], tests[i][3], tests[i][4]))
		{
			printf("Error: optimized does not match naive.\r\n");
			returnResult = -1;
		}
	}

	printf("\r\nTesting odd cases: \r\n");
	int oddTests[][5] = { { 400, 600, 3, 3, 7 }, { 600, 400, 4, 4, 7 }, { 501, 501, 4, 4, 7 }, { 751, 751, 4, 4, 4 } };
	for (int i = 0; i < ARRAY_SIZE(oddTests); i++)
	{
		printf("Testing %ix%i image, feature width %i, feature height %i, maximum diplacement %i... ", oddTests[i][0], oddTests[i][1], oddTests[i][2], oddTests[i][3], oddTests[i][4]);
		if (!benchmarkMatrix(oddTests[i][0], oddTests[i][1], oddTests[i][2], oddTests[i][3], oddTests[i][4]))
		{
			printf("Error: optimized does not match naive.\r\n");
			returnResult = -1;
		}
	}

	return returnResult;
}
