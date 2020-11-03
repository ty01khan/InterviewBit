#include <iostream>
#include <stack>
#include <cmath>

using namespace std;

ostream& bold_on(ostream& os)
{
	return os << "\e[1m";
}

ostream& bold_off(ostream& os)
{
	return os << "\e[0m";
}

int precd(char a)
{
	if(a == '+' || a == '-')
	{
		return 1;
	}
	else if(a == '*' || a == '/')
	{
		return 2;
	} 
	else if(a == '^')
	{
		return 3;
	}
	else
	{
		return 0;
	}
}

string infixTOpostfix(string infix)
{
	stack<char> s;
	s.push('#');
	string pf = "";
	
	int n = infix.size();
	
	for(int i = 0; i < n; i++)
	{
		if(isalnum(infix[i]))
			pf += infix[i];
		else if(infix[i] == '(')
			s.push('(');
		else if(infix[i] == '^')
			s.push('^');
		else if(infix[i] == ')')
		{
			while(s.top() != '#' && s.top() != '(')
			{
				pf += s.top();
				s.pop();
			}
			s.pop();
		}
		else
		{
			if(precd(infix[i]) > precd(s.top()))
				s.push(infix[i]);
			else
			{
				while(s.top() != '#' && precd(infix[i]) <= precd(s.top()))
				{
					pf += s.top();
					s.pop();
				}
				s.push(infix[i]);
			}
		}
	}
	while(s.top() != '#')
	{
		pf += s.top();
		s.pop();
	}
	
	return pf;
}

int main()
{
	string infix;
	cin >> infix;
	//string infix = "3+4-(60/2)*4";
	cout << "Postfix form of " << bold_on << infix << bold_off << " is " << bold_on << infixTOpostfix(infix) << bold_off << "\n";
	
	return 0;
}
