t = int(input())
for _ in range(t):
	s = input()
	x = int(input())
	l = len(s)
	w = ['']*l
	for j in range(l):
		i = j+1
		if s[i-1] == '1':
			if i > x and i+x <= len(s):
				w[i - 1 - x] = '1'
				w[i - 1 + x] = '1'
			elif i <= x and i+x <= len(s):
				w[i - 1 + x] = '1'
			elif i > x and i+x > len(s):
				w[i - 1 - x] = '1'
		else:
			if i > x and i+x <= len(s):
				w[i - 1 - x] = '0'
				w[i - 1 + x] = '0'
			elif i <= x and i+x <= len(s):
				w[i - 1 + x] = '0'
			elif i > x and i+x > len(s):
				w[i - 1 - x] = '0'
				
	a = 0
	W = ''
	for j in range(l):
		W += w[j]
		i = j+1
		if i > x and i+x <= len(s):
			if w[i - 1 - x] == '1' and w[i - 1 + x] == '1':
				if s[i-1] != '1':
					a = 1
					break
			if w[i - 1 - x] == '0' and w[i - 1 + x] == '0':
				if s[i-1] != '0':
					a = 1
					break
		elif i <= x and i+x <= len(s):
			if w[i - 1 + x] == '1':
				if s[i-1] != '1':
					a = 1
					break
			if w[i - 1 + x] == '0':
				if s[i-1] != '0':
					a = 1
					break
		elif i > x and i+x > len(s):
			if w[i - 1 - x] == '1':
				if s[i-1] != '1':
					a = 1
					break
			if w[i - 1 - x] == '0':
				if s[i-1] != '0':
					a = 1
					break
	
	if a == 1:
		print(-1)
	else:
		print(W)
