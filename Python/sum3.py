def main():
    A = list(map(int, input().split()))
    n = len(A)
    
    X = []
    
    for i in range(1,n-1):
        B = A[:i]
        C = A[i+1:]
        
        
        S1 = 0
        f1 = 0
        for j in range(len(B)):
            if B[j] > S1 and B[j] < A[i]:
                S1 = B[j]
                f1 = 1
        
        S2 = A[i]
        f2 = 0
        for k in range(len(C)):
            if C[k] > S2:
                S2 = C[k]
                f2 = 1
        
        if f1 == 1 and f2 == 1:
            X.append(A[i] + S1 + S2)
    return max(X)
    
if __name__ == '__main__':
   print( main())
