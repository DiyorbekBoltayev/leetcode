#Berilgan N soni ikkita tub sonni yig‘indisi bo‘lishini tekshiruvchi funksiya tuzing.
def toqm(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
n=int(input())
tub=[]
for i in range(1,n):
    if toqm(i):
        tub.append(i)
for i in tub:
    for j in tub:
        if i+j==n and i<j:
            print(i,j)

