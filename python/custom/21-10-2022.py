# 5. «Egar nuqta». A(m,n) sonli massiv berilgan. O’z satrida eng kichik bo’lgan element o’z ustunida eng katta bo’lsa,
# u egar nuqta deyiladi. Agar massivda egar
# nuqta bo’lsa, u yotgan satr va ustun raqamini, agar unday nuqta bo’lmasa, nol sonini chop eting.
javob=0
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("A=[")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(" {} ".format(a[i][j]),end="")
    print(" ")

print("]")
print("Egar nuqta:")

for i in range(len(a)):
    for j in range(len(a[0])):
        if min(a[i])==a[i][j]:
            bl=True
            for k in range(len(a)):
                if a[i][j] <a[k][j]:
                    bl=False
                    break
            if bl:
                javob="A[{},{}]".format(i+1,j+1)

print(javob)





