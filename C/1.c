#include<stdio.h>
#include<stdlib.h>

void f(int A[])
{
	int x = sizeof(A);  // x = 8?
	int y = sizeof(A[0]);
	printf("Function Value = %d %d %d\n", x,y,x/y);
	return;
}

int main()
{
	int A[4] = {1,2,3,4};
	f(A);
	int x = sizeof(A);	// x = 16?
	int y = sizeof(A[0]);
	printf("Main Value = %d %d %d\n", x,y,x/y);
	return 0;
}
