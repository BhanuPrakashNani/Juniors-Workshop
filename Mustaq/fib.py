def fibanocci(n):
	i=0
	a=0
	b=1
	for i in range(0,n):
		if(i<=1):
			c=i
		else:
			c=a+b
			a=int(b)
			b=int(c)
		print(c)
		i+=1
n=int(input())
fibanocci(n)

