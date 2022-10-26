n=int(input())
s=input()
a=[]

a=s.split()
for i in range(len(a)):
    a[i]=int(a[i])

yigindi=sum(a)

ortacha=yigindi/n
yi2=0
yi2soni=0
for i in a:
    if i<ortacha:
        yi2+=i
        yi2soni+=1
print("%.2f" %(yi2/yi2soni))