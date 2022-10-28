a=input()
b=[]
c=[]
print(len(a))
if int(len(a))/2 != 0:
    for i in range(1,len(a),2):
        b.append(a[i])
    for i in range(0,len(a),2):
        c.append(a[i])
else:
    for i in range(1,len(a),2):
         b.append(a[i])
    for i in range(0,len(a)+1,2):
        c.append(a[i])
print(b,c)
for i in c:
    print(i,end="")
for i in range(len(b),0,-1):
    print(c[i],end="")
