
och=['(','{','[']
yop=[')','}',']']

# (((}
def qavs(satr):
    satrlar=[]
    for i in satr:
        if i in och:
            satrlar.append(i)
        elif i in yop:
            if och[yop.index(i)]==satrlar[-1]:
                satrlar.pop()
    if satrlar==[]:
        print(True)
    else:
        print(satrlar)
qavs(input())
    
