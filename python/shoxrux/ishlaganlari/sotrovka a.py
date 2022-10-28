a=input()
a=['aa','wewe']
b=[2,0,]
d=a.split()
for i in range(len(d)-1):
    if d[i][0] == 'a':
        m=d[i]
        d.pop(i)
        d.append(m)
print(d)