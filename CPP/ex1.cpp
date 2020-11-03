#include <iostream>
using namespace std;

int fact(int n)
{
	if(n == 9)
	{
		return 1;
	}
	return n*fact(n-1);
}
int main()
{
	int x;
	cin >> x;
	cout << fact(x);
	return 0;
}
