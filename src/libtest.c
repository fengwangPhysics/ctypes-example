#include <stdio.h>
#include <stdlib.h>

void printData(double *data, int N) {
	int i;
	for (i=0; i<N; i++)
		printf("%f ", data[i]);
	putchar('\n');
}
