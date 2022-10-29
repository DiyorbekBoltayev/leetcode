import math
a=int(input())
b=input()
c=b.split()
for i in range(a):
    c[i]=int(c[i])
ekub=math.gcd(c[0],c[1])
for i in range(2,a):
    ekub=math.gcd(ekub,c[i])

print(ekub)