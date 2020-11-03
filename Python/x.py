def check(s):
    A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n = len(s)
    
    if s[0] == '?' and s[1] != '?':
        for i in range(26):
            if s[1] != A[i]:
                s[0] = A[i];
                break
    elif s[0] == '?' and s[1] == '?':
        s[0] = 'a'
    
    if s[n-1] == '?':
        if s[n-2] != '?':
            for j in range(26):
                if A[j] != s[n-2]:
                    s[n-1] = A[j]
                    break
        elif s[n-2] == '?':
            s[n-1] = 'a'
            
    cnt = 0
    for i in range(n):
        if s[i] == '?':
            cnt = 1
            break
    if cnt == 0:
        return s
    
    for i in range(len(s)):
        if s[i] == '?':
            if i != len(s)-1 and i != 0:
                if s[i-1] != '?' and s[i+1] != '?':
                    for j in range(26):
                        if A[j] != s[i-1] and A[j] != s[i+1]:
                            s[i] = A[j]
                            break
                elif s[i-1] != '?' and s[i+1] == '?':
                    for j in range(26):
                        if A[j] != s[i-1]:
                            s[i] = A[j]
                            break
                elif s[i-1] == '?' and s[i+1] != '?':
                    for j in range(26):
                        if A[j] != s[i+1]:
                            s[i] = A[j]
                            break
                else:
                    s[i] = 'a'
    
    
    if cnt == 1:
        return check(s)

if __name__ == '__main__':
    x = input()
    n = len(x)
    s = list(x)
    p = ''
    if n == 0:
        print('')
    elif n == 1:
        if s[0] == '?':
            print('a')
        else:
            print(s)
    else:
        s = check(s)
        for i in range(len(s)):
            p += s[i]
        print(p)
