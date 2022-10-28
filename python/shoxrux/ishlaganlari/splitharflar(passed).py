a=input()
d=a.split()
y=0
for i in range(len(d)):
    e=d[i]
    if e[0]==e[-1]:
        y+=1
    else:
        continue
print(y)