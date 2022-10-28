while True:
    a=['A','B','C','D','E']
    b=input()
    f=0
    for i in b:
        c= a.index(i)
        if f<=c:
            f+=1
        else:
            break
    if f<len(b):
        print('-1')
    else:
        print('True')