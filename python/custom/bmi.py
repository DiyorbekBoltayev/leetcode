s = input()
unli = ['a', 'i', 'u', 'e', 'o']
shart = False
soni = 0
for i in s:
    if i not in unli:
        soni += 1
    else:
        soni = 0
    if soni == 3:
        shart = True
        break
if shart:
    print('NO')
else:
    print('YES')
