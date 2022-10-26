m = int(input())
a = []
for i in range(m):
    a.append(input())
b = ['out', 'output', 'puton']
bb = ['in', 'input', 'one']
ans = a.copy()

for i in range(len(a)):

    while 'output' in a[i]:
        index = a[i].find('output')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 6:])

    while 'out' in a[i]:
        index = a[i].find('out')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 3:])

    while 'puton' in a[i]:
        index = a[i].find('puton')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 5:])

    while 'input' in a[i]:
        index = a[i].find('input')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 5:])

    while 'in' in a[i]:
        index = a[i].find('in')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 2:])

    while 'one' in a[i]:
        index = a[i].find('one')
        if index != -1:
            a[i] = str(a[i][0:index] + a[i][index + 3:])
    if len(a[i]) == 0:
        ans[i] = "YES"
    else:
        ans[i] = "NO"
        
for i in range(len(ans)):
    print(ans[i])
