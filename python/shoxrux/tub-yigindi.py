def tubmi(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


n = int(input('n:'))
yoq = True
for i in range(1, n // 2 + 1):
    if tubmi(i) and tubmi(n - i):
        print('Yes')
        yoq = False
        break
if yoq: print('No')
