s = input()
V = ['a','e','i','o','u']

l = []
for x in s:
	if x in V:
		s = s.replace(x,'')

print(s)
		
