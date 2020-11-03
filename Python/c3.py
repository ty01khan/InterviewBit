import numpy as np
s = input()
n = len(s)

f = np.zeros(26, dtype = np.int)

for j in range(n):
	f[ord(s[j]) - ord('a')] += 1

for j in range(n):
	if f[ord(s[j]) - ord('a')]:
		print(s[j], '->', f[ord(s[j])- ord('a')])
		f[ord(s[j])- ord('a')] = 0
