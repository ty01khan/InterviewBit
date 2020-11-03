#include <iostream>
#include <vector>
using namespace std;

vector<int> merge(vector<int> a, vector<int> b)
{
	int na = a.size(), nb = b.size();
	int i = 0, j = 0,  k = 0;
	vector<int> result(na+nb);
	
	while(i < na && j < nb)
	{
		if(a[i] < b[j])
		{
			result[k] = a[i];
			i++;
		}
		else
		{
			result[k] = b[j];
			j++;
		}
		k++;
	}
	
	while(i < na)
	{
		result[k] = a[i];
		i++;
		k++;
	}
	
	while(j < nb)
	{
		result[k] = b[j];
		j++;
		k++;
	}
	
	return result;
}

int main()
{
	vector<int> a;
	vector<int> b;
	
	int x, k;
	
	cout << "Enter elements for Vector a : ";
	cin >> x;
	while(x != 0)
	{
		a.push_back(x);
		cin >> x;
	}
	
	cout << "Enter elements for Vector b : ";
	cin >> x;
	while(x != 0)
	{
		b.push_back(x);
		cin >> x;
	}
	
	vector<int> result = merge(a,b);
	
	k = a.size() + b.size();
	for(int i = 0; i < k; i++)
	{
		cout << result[i] << " ";
	}
	cout << "\n";
	return 0; 
}
