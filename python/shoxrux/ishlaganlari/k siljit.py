a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=input()
c=int(input())
l=[]
for i in b:
	l.append(i)
e=l[c-1]
for i in a:
    if e==i:
        h=a.index(i)
        l[c-1]=a[h+2]

for i in l:
	print(i,end='')