def tubmi(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


for i in range(100, 1000):
    if tubmi(i):
        if tubmi(i + 2):
            print(i, i + 2)
