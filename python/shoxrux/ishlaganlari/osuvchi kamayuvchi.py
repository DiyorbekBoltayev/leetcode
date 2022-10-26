#10.  Sonni raqamlarini o‘sish (kamayish) tartibida saralovchi funksiya tuzing.
n=input()
s=[]

for i in n:
    s.append(i)
a=s.copy()
s.sort()
a.sort(reverse=True)
for i in s:
    print(i,end="")
print("\n")
for i in a:
    print(i, end="")