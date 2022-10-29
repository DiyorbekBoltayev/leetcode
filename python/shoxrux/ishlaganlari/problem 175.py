a=input()
r=[]
e=[]
s=True
for i in a:
    r.append(i)
for i in a:
    if i == '(':
            s=False
            q=int(r.index('('))
            w=int(r.index(')'))
            y=r[w-1:q:-1]
            r.pop(q)
            r.pop(w-1)
            for j in y:
                e.append(j)
    elif i ==')':
            s=True
            continue
    elif s:
        e.append(i)
for i in e:
    print(i,end='')