a=input()
b=a.split()
if int(b[0]>b[1]):
    print('>')
elif int(b[0]<b[1]):
    print('<')
else:
    print('=')