# Your code here
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

if __name__ == '__main__':
	Q = int(input())
	for _ in range(Q):
		N, K = map(int, input().split())
		if N == K:
			result = fact(N)**2
		else:
			result = (fact(N))**2/(N-K)
			result = int(result)
		print(result)
