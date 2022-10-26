a=int(input('a='))
k=int(input('k='))
l=int(input('l='))
b=[]
while a>9:
    b.insert(0,a%10)
    a=a//10
b.insert(0,a)
d=b[k-1]
b[k-1]=b[l-1]
b[l-1]=d
for i in b:
    print(i,end="")
