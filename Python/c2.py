A = list(map(int, input().split()))
Sum = int(input())
n = len(A)
A.sort()

i = n-1
while i > 1:
	j = 0
	k = i-1
	
	while j < k:
		if A[i]+A[j]+A[k] > Sum:
			k -= 1
		elif A[i]+A[j]+A[k] < Sum:
			j += 1
		else:
			print(A[i], A[j], A[k])
			k -= 1
			j += 1
	i -= 1

