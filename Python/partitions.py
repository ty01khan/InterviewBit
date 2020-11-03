'''
Problem Description

You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])



Problem Constraints

1 <= A <= 105

-109 <= B[i] <= 109



Input Format

First argument is an integer A.

Second argument is an 1D integer array B of size A.



Output Format

Return a single integer denoting the number of ways to split the array B into three parts with the same sum.


Example Input

Input 1:

 A = 5
 B = [1, 2, 3, 0, 3]

Input 2:

 A = 4
 B = [0, 1, -1, 0]



Example Output

Output 1:

 2

Output 2:

 1



Example Explanation

Explanation 1:

 There are no 2 ways to make partitions -
 1. (1,2)+(3)+(0,3).
 2. (1,2)+(3,0)+(3).

Explanation 2:

 There is only 1 way to make partition -
 1. (0)+(-1,1)+(0).

'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, n, a):
        cnt = [0 for i in range(n)] 
        s = 0
      
        # Calculating the sum of the array 
        # and storing it in variable s 
        s = sum(a) 
      
        # Checking s is divisible by 3 or not 
        if (s % 3 != 0): 
            return 0
      
        # Calculating the sum of each part 
        s //= 3
      
        ss = 0
      
        # If the sum of elements from i-th  
        # to n-th equals to sum of part  
        # putting 1 in cnt array otherwise 0. 
        for i in range(n - 1, -1, -1): 
      
            ss += a[i] 
            if (ss == s): 
                cnt[i] = 1
      
        # Calculating the cumulative sum 
        # of the array cnt from the last index. 
        for i in range(n - 2, -1, -1): 
            cnt[i] += cnt[i + 1] 
      
        ans = 0
        ss = 0
      
        # Calculating answer using original 
        # and cnt array. 
        for i in range(0, n - 2): 
            ss += a[i] 
            if (ss == s): 
                ans += cnt[i + 2] 
      
        return ans 
