// CPP program to count words in a string 
// using stringstream. 
#include <bits/stdc++.h> 
using namespace std; 
  
int countWords(string str) 
{ 
    // breaking input into word using string stream 
    stringstream s(str); // Used for breaking words 
    string word; // to store individual words 
  
    int count = 0; 
    while (s >> word) 
    	cout << word << "\n";
        count++; 
    cout << "\n";
    cout << "Number of words are: " << count << "\n";
} 
  
// Driver code 
int main() 
{ 
    string s;
    getline(cin,s);
    countWords(s); 
    return 0; 
} 

