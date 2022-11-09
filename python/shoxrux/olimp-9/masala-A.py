d=input()
d=d.split()
a=d[0]
b=d[1]
a1=[]
b1=[]
if a[0]=='a':
    a=f'{1},{a[1]}'
if a[0]=='b':
    a=f'{2},{a[1]}'
if a[0]=='c':
    a=f'{3},{a[1]}'
if a[0]=='d':
    a=f'{4},{a[1]}'
if a[0]=='e':
    a=f'{5},{a[1]}'
if a[0]=='f':
    a=f'{6},{a[1]}'
if a[0]=='g':
    a=f'{7},{a[1]}'
if a[0]=='h':
    a=f'{8},{a[1]}'
if b[0]=='a':
    b=f'{1},{b[1]}'
if b[0]=='b':
    b=f'{2},{b[1]}'
if b[0]=='c':
    b=f'{3},{b[1]}'
if b[0]=='d':
    b=f'{4},{b[1]}'
if b[0]=='e':
    b=f'{5},{b[1]}'
if b[0]=='f':
    b=f'{6},{b[1]}'
if b[0]=='g':
    b=f'{7},{b[1]}'
if b[0]=='h':
    b=f'{8},{b[1]}'
step=1
t=True
for i in a:
    a1.append(i)
for i in b:
    b1.append(i)
while t:
    if int(a1[0])-int(b1[0])>2 or int(a1[0])-int(b1[0])<-2 and int(a1[2])-int(b1[2])>2 or int(a1[2])-int(b1[2])<-2:
        step+=1
        a1[0]==int(a1[0])+2
        a1[2]=int(a1[2])+2
    else:
        t=False
print(step)