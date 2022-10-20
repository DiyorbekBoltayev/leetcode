k1=input('fil kordinatasi:').split(' ')
k2=input('dona kordinatasi:').split(' ')
if abs(int(k1[0]) - int(k2[0])) == abs(int(k1[1])-int(k2[1])):
    print('yes')
else:
    print('no')
