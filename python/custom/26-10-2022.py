massiv = input('Massiv elementlarini probel bilan ajratilgan holda kiriting:')
massiv = massiv.split()
for i in range(len(massiv)):
    massiv[i] = int(massiv[i])
print("Topshiriq 1")
manfiy_soni = 0
for i in massiv:
    if i < 0:
        manfiy_soni += 1
print("Manfiy sonlar soni:", manfiy_soni)
print("Topshiriq 2")
b = massiv.copy()
for i in range(len(b)):
    b[i] = abs(b[i])
indeks = b.index(min(b))
summa = 0
for i in range(indeks + 1, len(massiv)):
    summa += massiv[i]

print(summa)
print("Topshiriq 3")
for i in range(len(massiv)):
    if massiv[i] < 0:
        massiv[i] = massiv[i] ** 2
massiv.sort()
print("Massiv:", massiv)

mx = max(massiv)
m = mx / 5
for i in range(len(massiv)):
    if abs(massiv[i] - mx) == m:
        k=massiv[i]
        massiv.pop(i)
        massiv.insert(0,k)

print(massiv)