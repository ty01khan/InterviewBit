def makeDiv(a, b):
	if a%b == 0:
		return 1
	return 0
	
def main():
	N, K = map(int, input().split())
	X = int((2**104 - 16)/15)
	
	cnt = 0
	i = 1
	while True:
		if makeDiv(i*X, 2**K) == 1:
			break
		cnt += 1
		i *= N
	return cnt
	
if __name__ == '__main__':
	print(main())
