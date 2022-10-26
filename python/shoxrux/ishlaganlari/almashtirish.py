# Berilgan sonni K o‘rindagi raqamini N o‘rindagi raqami bilan almashtiruvchi funksiya tuzing.
a=input()
k=int(input())
n=int(input())
c=[]
for i in a:
    c.append(i)
c[k-1],c[n-1]=c[n-1],c[k-1],
for i in c:
    print(i,end="")

