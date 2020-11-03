/* Implement a program to Merge all the arrays and sort in ascending order.

Input:
3 4
5 8 4 7
15 32 87 65
2 1 78 91

3 - no of arrays to be merged 
4- no of elements in an array

Output: 1 2 4 5 7 8 15 32 65 78 87 91 
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int nA, n, x;
    cin >> nA >> n;
    vector<int> A;
    
    for(int i = 0; i < nA; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin >> x;
            A.push_back(x);
        }
    }
    n = A.size();
    sort(A.begin(), A.end());
    for(int i = 0; i < n; i++)
    {
        cout << A[i] << " ";
    }
    cout << "\n";
    return 0;
}
