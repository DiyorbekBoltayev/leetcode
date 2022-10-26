n=int(input())
a=input()
a=a.split()
a=list(map(int,a))
b=int(min(a))
for i in a:
	i=int(i)
	c=i/b
	print("%.2f" %c,end=" ")