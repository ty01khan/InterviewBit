#include<iostream>
#include<string>
using namespace std;

int main()
{
	string str;
	
	cout << "Please enter you name : ";
	getline(cin, str);
	
	cout << "Hello " << str << ", welcome to C++ coding !\n";
	
	return 0;
}
