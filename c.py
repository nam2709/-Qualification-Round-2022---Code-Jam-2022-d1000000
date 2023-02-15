N = int(input())
for e in range(1,N+1):
	T = int(input())
	# nhap nhieu input
	a = list(map(int, input().split()))
	b = sorted(a)
	# so sanh a[i] với vị trí của nó

	for i in range(0,T):
		if i+1 > b[i]:
			b.pop(i)
			break
	c = len(b)
	if c > max(b):
		c = max(b)
	print("Case #"+str(e)+": "+str(c))