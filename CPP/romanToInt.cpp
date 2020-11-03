'''


Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more
details about roman numerals at Roman Numeric System



Input Format

The only argument given is string A.

Output Format

Return an integer which is the integer verison of roman numeral string.

For Example

Input 1: A = "XIV"
Output 1: 14

Input 2: A = "XX"
Output 2: 20


'''

int Solution::romanToInt(string A) {
    int n = A.size();
    int res[n], cnt = 0;
    for(int i = 0; i < n; i++) {
        if(A[i] == 'I')
            res[i] = 1;
        else if(A[i] == 'V')
            res[i] = 5;
        else if(A[i] == 'X')
            res[i] = 10;
        else if(A[i] == 'L')
            res[i] = 50;
        else if(A[i] == 'C')
            res[i] = 100;
        else if(A[i] == 'D')
            res[i] = 500;
        else if(A[i] == 'M')
            res[i] = 1000;
    }
    
    if(n == 1) { return res[0]; }
    
    int i = 0;
    while(i < n-1) {
        if(res[i] < res[i+1]) {
            cnt += res[i+1] - res[i];
            i += 2;
        }
        else {
            cnt += res[i];
            i += 1;
        }
    }
    if(res[n-1] <= res[n-2]) {
        cnt += res[n-1];
    }
    
    return cnt;
}

