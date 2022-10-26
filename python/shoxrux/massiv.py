n = int(input('n='))
a = [0] * n

a[0] = int(input('a[0]='))
max = a[0]
min = a[0]

for i in range(1, n):
    a[i] = int(input('a[{}]='.format(i)))
    if a[i] > max:
         max = a[i]
    if a[i] < min:
         min = a[i]

print(max, min)
