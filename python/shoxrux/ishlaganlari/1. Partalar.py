a = input()
s = a.split()
d = 0


def juft(j):
    j = int(j)
    if j % 2 == 0:
        return True
    else:
        return False


for i in s:
    i = int(i)
    if juft(i):
        d += i / 2
    else:
        d += (i + 1) / 2
print(int(d))
