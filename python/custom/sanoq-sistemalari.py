print('Sanoq sistemalari ustida ammallar bajarish.')


def onlikdan_binariga(a):
    b = []
    while True:
        if a == 0:
            break
        else:
            b.append(a % 2)
            a = a // 2
    b.reverse()
    s = ''
    for i in b:
        s += str(i)
    return s


def binaridan_onlikka(a):
    b = 0
    a = list(a)
    a.reverse()
    for i in range(len(a)):
        b += int(a[i]) * 2 ** i
    return b


def onlikdan_sakkizlikka(a):
    b = []
    while True:
        if a == 0:
            break
        else:
            b.append(a % 8)
            a = a // 8
    b.reverse()
    s = ''
    for i in b:
        s += str(i)
    return s


def sakizlikdan_onlikka(a):
    b = 0
    a = list(a)
    a.reverse()
    for i in range(len(a)):
        b += int(a[i]) * 8 ** i
    return b


def onlikdan_onoltikka(a):
    b = []
    while True:
        if a == 0:
            break
        else:
            b.append(a % 16)
            a = a // 16
    b.reverse()
    return b



def onoltikdan_onlikka(a):
    b = 0
    a = list(a)
    a.reverse()
    for i in range(len(a)):
        b += int(a[i]) * 16 ** i
    return b
def onoltikka_tarjima(a):
    b = []
    for i in a:
        if i == 10:
            b.append('A')
        elif i == 11:
            b.append('B')
        elif i == 12:
            b.append('C')
        elif i == 13:
            b.append('D')
        elif i == 14:
            b.append('E')
        elif i == 15:
            b.append('F')
        else:
            b.append(i)
    return b
def onoltilikdan_tarjima(a):
    b = []
    for i in a:
        if i == 'A':
            b.append(10)
        elif i == 'B':
            b.append(11)
        elif i == 'C':
            b.append(12)
        elif i == 'D':
            b.append(13)
        elif i == 'E':
            b.append(14)
        elif i == 'F':
            b.append(15)
        else:
            b.append(i)
    return b

buyruq = ""
while True:
    print("Quyidagi buyruqlardan birini tanlang:\n")
    print("1. O'nlikdan ikkilikka o'tkazish.")
    print("2. Ikkilikdan o'nlikka o'tkazish.")
    print("3. O'nlikdan sakizlikka o'tkazish.")
    print("4. Sakizlikdan o'nlikka o'tkazish.")
    print("5. O'nlikdan o'noltikka o'tkazish.")
    print("6. O'noltikdan o'nlikka o'tkazish.")
    print("7. Ikkilikdan sakkizlikka.")
    print("8. Sakkizlikdan ikkilikka.")
    print("9. Ikkilikdan o'noltikka.")
    print("10. O'noltikdan ikkilikka.")
    print("11. Sakizlikdan o'noltikka.")
    print("12. O'noltikdan sakizlikka.")
    print("13. Dasturdan chiqish.")
    buyruq = input('>>> ')
    if buyruq == "1":
        a = int(input("O'nlik son kiriting: "))
        print(onlikdan_binariga(a))
    elif buyruq == "2":
        a = input("Ikkilik son kiriting: ")
        print(binaridan_onlikka(a))
    elif buyruq == "3":
        a = int(input("O'nlik son kiriting: "))
        print(onlikdan_sakkizlikka(a))
    elif buyruq == "4":
        a = input("Sakizlik son kiriting: ")
        print(sakizlikdan_onlikka(a))
    elif buyruq == "5":
        a = int(input("O'nlik son kiriting: "))
        son=onoltikka_tarjima(onlikdan_onoltikka(a))
        for i in son:
            print(i,end='')
        print()
    elif buyruq == "6":
        a = input("O'noltik son kiriting: ")
        print(onoltikdan_onlikka(onoltilikdan_tarjima(a)))
    elif buyruq == "7":
        a = input("Ikkilik son kiriting: ")
        print(onlikdan_sakkizlikka(binaridan_onlikka(a)))
    elif buyruq == "8":
        a = input("Sakizlik son kiriting: ")
        print(onlikdan_binariga(sakizlikdan_onlikka(a)))
    elif buyruq == "9":
        a = input("Ikkilik son kiriting: ")
        son=onoltilikdan_tarjima(onlikdan_onoltikka(binaridan_onlikka(a)))
        for i in son:
            print(i,end='')
        print()
    elif buyruq == "10":
        a = input("O'noltik son kiriting: ")
        print(onlikdan_binariga(onoltikdan_onlikka(onoltilikdan_tarjima(a))))
    elif buyruq == "11":
        a = input("Sakizlik son kiriting: ")
        son=onoltikka_tarjima(onlikdan_onoltikka(sakizlikdan_onlikka(a)))
        for i in son:
            print(i,end='')
        print()
    elif buyruq == "12":
        a = input("O'noltik son kiriting: ")
        print(onlikdan_sakkizlikka(onoltikdan_onlikka(onoltilikdan_tarjima(a))))

    elif buyruq == "13":
        break
