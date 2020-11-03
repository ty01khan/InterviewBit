def fib(n, lookup):
	if n <= 1:
		return n
	
	if n not in lookup:
		lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
	print(lookup)
	return lookup[n]

if __name__ == '__main__':
	n = 9
	lookup = {}
	print(fib(n, lookup))
