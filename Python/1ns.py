def findMinCost(Cost, K):
	l = len(Cost)
	Cost.sort()
	return sum(Cost[:K-1])

def main():
	N, K, J = map(int, input().split())
	C = list(map(int, input().split()))
	newC = C[:J-1] + C[J:]
	minPrice = C[J-1] + findMinCost(newC, K)
	print(minPrice)
	
if __name__ == '__main__':
	main()
