n = int(input('n='))
soni3 = 0
soni5 = 0
butun3 = n // 3
butun5 = n // 5
f = False
for i in range(0, butun3 + 1):
    for j in range(0, butun5 + 1):
        if i * 3 + j * 5 == n:
            print([3]*i, [5]*j)
            f = True
            break

if f:
    print('ha')
else:
    print('yoq')
