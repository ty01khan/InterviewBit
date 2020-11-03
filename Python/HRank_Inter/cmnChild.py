
s1 = input()
s2 = input()

n = len(s1)
c1 = 0
c2 = 0
for i in range(n):
	if s1[i] in s2:
		c1 += 1
		a = s2.index(s1[i])
		break
		
		
if c1 == 1:
	for j in range(i+1, n):
		for k in range(a+1, n):
			if s1[j] == s2[k]:
				print(s1[j])
				c1 += 1
				i = j
				a = k
				break

for i in range(n):
	if s2[i] in s1:
		a = s1.index(s2[i])
		c2 += 1
		break
		
		
if c2 == 1:
	for j in range(i+1, n):
		for k in range(a+1, n):
			if s2[j] == s1[k]:
				c2 += 1
				i = j
				a = k
				break
print(max(c1,c2))
