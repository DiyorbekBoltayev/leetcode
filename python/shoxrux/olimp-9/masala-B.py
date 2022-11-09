import random

a = input()
a = a.split()

alifbo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
satr = ''
for j in range(26):
    a[j] = int(a[j])
    satr = f'{satr}{a[j] * alifbo[j]}'
satr = list(satr)


if sum(a)==1:
    print(alifbo[a.index(1)])
    exit()


w = True
while w:
    for i in range(len(satr) - 1):
        i = int(i)
        t = True
        while t:

            if satr[i] == satr[i + 1]:
                satr.insert(random.randrange(satr.index(satr[i]) + 1, len(satr)), satr[i])
                satr.pop(i)
            else:
                t = False
        else:
            w = False

for i in satr:
    print(i, end='')