def dl(num):
    a = 0
    for i in range (len(num)):
        a = (a + int(num[i])) % 9
    if a == 0:
        return 9
    else:
        return a % 9
 
num = input()
a=num.split()

print (dl(a[0]),' ',dl(a[1]))