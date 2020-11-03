def lcs (X, Y, m, n):
	if m == 0 or n == 0:
		return 0
	
	if X[m-1] == Y[n-1]:
		return lcs (X, Y, m-1, n-1) + 1
	
	return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))
	
if __name__ == '__main__':
	X = input("Please enter first string : ")
	Y = input("Please enter second string : ")
	m = len(X)
	n = len(Y)
	print("Maximum Subsequence of X and Y is :", lcs(X, Y, m, n))
