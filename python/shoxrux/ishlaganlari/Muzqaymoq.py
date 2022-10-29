a = int(input())
w = True
while w:
    if a >= 5:
        if a % 3 != 0:
            a -= 5
        else:
            a -= 3
    elif a >= 3:
        a -= 3
    else:
        w = False
print(a == 0)
