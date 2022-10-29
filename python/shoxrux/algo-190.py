n=int(input())
sekund=0;
while n>1:
    if n%3 ==0 :
        n=n/3
        sekund+=1
    elif n%3==1:
        n-=1
        sekund+=1
    elif n%2 ==0 :
        n=n/2
        sekund+=1
    elif n%3==2:
        n-=1
        sekund+=1
    else:
        n=n-1
        sekund+=1
    print(n)

print(sekund)