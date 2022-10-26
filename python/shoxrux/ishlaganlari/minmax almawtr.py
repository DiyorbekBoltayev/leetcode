a=['5','2','3','4']
b=min(a)
oxiri=len(a)-1
index=a.index(b)
a[index],a[oxiri]=a[oxiri],a[index]
print(a)