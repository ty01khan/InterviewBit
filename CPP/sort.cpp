#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

int main() {
	int A[8], i = 0;
	
	while(i < 8) {
		cin >> A[i];
		i++;
	}
	cout << A[3] << "\n";
	int n = sizeof(A)/sizeof(A[0]);
	sort(A, A+n, greater <int> ());
	
	i = 0;
	while(i < 8) {
		cout << A[i] << " ";
		i++;
	}
	cout << "\n";
	return 0;
}
