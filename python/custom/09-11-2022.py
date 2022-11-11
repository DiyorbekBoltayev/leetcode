print('1.  Stek birinchi va oxirgi elementlari o„rni almashtirilsin. ')
a = [1, 2, 3, 4, 5]
a[0], a[-1] = a[-1], a[0]
print(a)
print('2.  Stek elementlari teskari tartibda joylashtirib chiqilsin. ')
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
print('3.Stek o„rtasidagi element o„chirib tashlansin. Agar stek elementi toq bo„lsa, bitta element, aks holda ikkita element o„chirilsin. ')
a = [1, 2,  3, 4, 5]
n=len(a)
if n%2==0:
    a.pop(n//2)
    a.pop(n//2 -1)
else:
    a.pop(n//2)
print(a)


