#17.  Ikkita son berilgan. Ularning raqamlaridan soni ko‘pini toping. Sonni raqamlari sonini topuvchi funksiya tuzing.
def soni(a,b):
    a=len(a)
    b=len(b)
    if a>b:
        return a
    else: return b
a1=input()
a2=input()
b=soni(a1,a2)
if b==len(a1):
    print(a1)
else: print(a2)

