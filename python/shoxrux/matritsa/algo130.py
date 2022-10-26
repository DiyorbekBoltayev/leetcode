s = input()
s = s.split()


m = int(s[1])
n = int(s[0])
a = [[0] * m] * n;
for i in a:
    print(i)

for k in range(n):

    for j in range(m):
        a[k][j] = "{},{}".format(k, j)

    for i in a:
        print(i)
    print()



