BINARIES = benchmark check depthMap
CC = gcc
CFLAGS = -O3 -DNDEBUG -g0 -std=c99 -Wall -march=corei7 -maes -mpclmul -mpopcnt -fopenmp -pthread
LFLAGS = -lm -lpthread

default: clean check benchmark

debug: clean all_debug

all: $(BINARIES)

all_debug: CC += -DDEBUG -ggdb3
all_debug: all

benchmark: benchmark.o calcDepthNaive.o calcDepthOptimized.o utils.o
	$(CC) $(CFLAGS) -o $@ $^ $(LFLAGS)

check: calcDepthNaive.o calcDepthOptimized.o check.o utils.o
	$(CC) $(CFLAGS) -o $@ $^ $(LFLAGS)

depthMap: calcDepthNaive.o calcDepthOptimized.o depthMap.o utils.o
	$(CC) $(CFLAGS) -o $@ $^ $(LFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $*.c

clean:
	rm -rf *.o
	rm -rf $(BINARIES)
