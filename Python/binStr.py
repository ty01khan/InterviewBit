t = int(input())
for _ in range(t):
	s = input()
	x = int(input())
	w = ['']*len(s)
	for j in range(len(s)):
		i = j+1
		if s[i] == '0':
			if i+1 > x and i+x+1 <= len(s):
				w[i-x] = '0'
				w[i+x] = '0'
			elif i+1 <= x and i+x+1 <= len(s):
				w[i+x] = '0'
			elif i+1 > x and i+x+1 > len(s):
				w[i-x] = '0'
		else:
			if i+1 > x and i+x+1 <= len(s):
				w[i-x] = '1'
				w[i+x] = '1'
			elif i+1 <= x and i+x+1 <= len(s):
				w[i+x] = '1'
			elif i+1 > x and i+x+1 > len(s):
				w[i-x] = '1'
	a = 0
	for i in range(len(s)):
		if w[i] == '':
			a = 1
			break
	if a == 1:
		print(-1)
	else:
		W = ''
		for i in range(len(w)):
			W += w[i]
		print(W)
