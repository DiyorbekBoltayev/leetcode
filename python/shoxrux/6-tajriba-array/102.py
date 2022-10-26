n=int(input())
s=input()
ab=input()
a=s.split()
b=ab.split()
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(b)):
    b[i]=int(b[i])
k=min(a)
for i in range(b[0]-1,b[1]):
    a[i]/=k
for i in a:
    print("%.1f" %i,end=" ")