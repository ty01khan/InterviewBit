import random 
  
# Function generates N random integers from arr
def shuffle (arr, N):
	sArr = []
	for i in range(N):
		rIdx = random.randint(i, N-1)
		
		arr[i],arr[rIdx] = arr[rIdx],arr[i]
		sArr.append(arr[i])
	return sArr

def main():
	arr = list(map(int, input("Please enter any list of integers: ").split()))
	A = len(arr)
	
	N = int(input("Enter N: "))
	
	while N > A:
		print("Error : N should be less than", A)
		N = int(input("Enter N: "))
		
	sArr = shuffle(arr, N)
	print(sArr)

if __name__ == '__main__':
	main()
