n=int(input())
a=0
r=True
while r:
    if int(n)==1:
        r=False
        break
    elif n%3==0:
        n-=(n-n/3)
        a+=1
    elif n%2==0:
        n-=(n-n/2)
        a+=1
    else:
        n-=1
        a+=1
print(a)


