/* 
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

    It contains no unmatched brackets.
    The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

Given

strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced or NO if it is not.

isBalanced has the following parameter(s):

    s: a string of brackets

Input Format

The first line contains a single integer
, the number of strings.
Each of the next lines contains a single string

, a sequence of brackets.

Constraints

, where

    is the length of the sequence.
    All chracters in the sequences ∈ { {, }, (, ), [, ] }.

Output Format

For each string, return YES or NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output

YES
NO
YES

Explanation

    The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
    The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
    The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.

*/

#include <bits/stdc++.h>

using namespace std;

// Complete the isBalanced function below.
string isBalanced(string s) {
    stack<char> v;
    
    if(s.size() == 0)
    {
        return "YES";
    }
    else if(s[0] == ')' || s[0] == '}' || s[0] == ']')
    {
        return "NO";
    }

    int cnt = 0, i = 0;
    while(s[i]!= '\0')
    {
        if(s[i] == '{' || s[i] == '(' || s[i] == '[')
        {
            v.push(s[i]);
        }
        else
        {
            if(v.empty())
            {
                cnt = 1;
                break;
            }
            char c = v.top();
            v.pop();
            if(s[i] == ')')
            {
                if(c != '(')
                {
                    cnt = 1;
                    break;
                }
            }
            else if(s[i] == '}')
            {
                if(c != '{')
                {
                    cnt = 1;
                    break;
                }
            }
            else if(s[i] == ']')
            {
                if(c != '[')
                {
                    cnt = 1;
                    break;
                }
            }
        }
        i++;
    }
    if(!v.empty() || cnt == 1)
    {
        return "NO";
    }
    return "YES";
}

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        string s;
        cin >> s;

        string result = isBalanced(s);

        cout << result << "\n";
    }

    return 0;
}
