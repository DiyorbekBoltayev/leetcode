#16.  Ikkita son berilgan. Ularni raqamlari yig‘indisi kattasini toping. Sonni raqamlari yig‘indisini topuvchi funksiya tuzing.
def yigindi(a):
    a=str(a)
    w=0
    for i in a:
        i=int(i)
        w+=i
    return w
a1=input()
aa1=int(yigindi(a1))
a2=input()
aa2=int(yigindi(a2))
if aa1>aa2:
    print(a1)
else: print(a2)
