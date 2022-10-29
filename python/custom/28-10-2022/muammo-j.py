x1=input('shox kordinatasini kiriting:')
x1=x1.split()
k1=int(x1[0])
k2=int(x1[1])
x2=input('katak kordinatasini kiriting:')
x2=x2.split()
d3=int(x2[0])
d4=int(x2[1])

if abs(k1-d3)==abs(k2-d4)==1 or abs(k1-d3)==1 and k2==d4 or abs(k2-d4)==1 and k1==d3:
    print('HA')
else:
    print('YOQ')