'''
Largest Number formed from an Array

Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.

Input:
The first line of input consists number of the test cases. The description of T test cases is as follows:
The first line of each test case contains the size of the array, and the second line has the elements of the array.

Output:
In each separate line print the largest number formed by arranging the elements of the array in the form of a string.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 102
0 ≤ A[i] ≤ 103

Example:
Input:
2
5
3 30 34 5 9
4
54 546 548 60

Output:
9534330
6054854654
'''
#code

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    
    B = []
    
    for i in range(N):
        for j in range(i+1,N):
            if str(A[i])+str(A[j]) < str(A[j])+str(A[i]):
                a = A[i]
                A[i] = A[j]
                A[j] = a
    
    tot = ''
    for i in range(N):
        tot += str(A[i])
    
    print(tot)
