def balancedParn(S):
	Open = ['(', '{', '[']
	Close = [')', '}', ']']
	stack = []
	
	for x in S:
		if x in Open:
			stack.append(x)
		
		else:
			if len(stack) > 0:
				i = Close.index(x)
				if stack[len(stack)-1] == Open[i]:
					stack.pop()
				
				else:
					return False
			else:
				return False
				
	if len(stack) == 0:
		return True
	else:
		return False
				
	
if __name__ == '__main__':
	String = input()
	print(balancedParn(String))
