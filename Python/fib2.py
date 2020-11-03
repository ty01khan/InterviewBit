def fib(n):
	if n <= 1:
		return n;
	
	last = 1
	secLast = 0
	for i in range(n):
		new = last + secLast
		secLast = last
		last = new
	return last

if __name__ == '__main__':
	n = 8
	print(fib(n))
