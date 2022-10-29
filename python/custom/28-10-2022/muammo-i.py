x1=input('ferzi kordinatasini kiriting:')
x1=x1.split()
k1=x1[0]
k2=x1[1]
x2=input('dona kordinatasini kiriting:')
x2=x2.split()
d3=x2[0]
d4=x2[1]
if k1==d3 or k2==d4 or abs(int(k1)-int(d3))==abs(int(k2)-int(d4)):
    print('HA')
else:
    print('YOQ')