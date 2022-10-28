n=input()
# '1' '2'....
# 1 2 3 6 2 4 4
#-33 -23 1 4 5 7 10
# boshdagi 2si va oxirgisi ko'paytmasini oxirgi 3-si ko'paytmasi bn solishtirish kk
d=n.split()
mx=max(d)
y=int(d.index(mx))
d.pop(y)
max1=max(d)
y=int(d.index(max1))
d.pop(y)
max2=max(d)
y=int(d.index(max2))
d.pop(y)
print(int(mx)*int(max1)*int(max2))