#include <bits/stdc++.h> 
using namespace std; 
  
int main() 
{ 
    vector<int> v;
    int x;
    
    cout << "Enter numbers : ";
    
    cin >> x;
  	while(x != 0)
  	{
  		v.push_back(x);
  		cin >> x;
  	}
  		
    sort(v.begin(), v.end(), greater<int>()); 
  
    cout << "Sorted : "; 
    for (auto x : v) 
        cout << x << " "; 
  	cout << "\n";
  	
    return 0; 
}
