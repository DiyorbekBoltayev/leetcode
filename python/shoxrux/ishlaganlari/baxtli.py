def xisobla(b):

    p, o = 0, 0
    for i in range(3):
        p += int(b[i])
    for i in range(3, 6):
        o += int(b[i])
    if p == o:
        return True
    else:
        return False


for k in range(100000, 1000000):
    if xisobla(str(k)):
        print(k)
