import random

suzlar = ['mehanizatsya', 'odamlar', 'murakkab', 'qiyinchilik','bahromjon']
i = random.randint(0, len(suzlar) - 1)
suz = suzlar[i]
shifr = '*' * len(suz);

ochko = 15
print('Sizda {} ta ochko bor.'.format(ochko))
print('Har bir ochko bir imkoniyat !')
print('Sizga so\'z berildi. Uning uzunligi {} ta harf'.format(len(suz)))
while ochko > 0:
    print('Harflarini toping:')
    print(shifr)
    print('Harf kiriting:')
    harf = input()
    if harf in suz:
        print('Harf topdingiz')

        for i in range(len(suz)):
            if suz[i] == harf:
                shifr = shifr[:i] + harf + shifr[i + 1:]
        print(shifr)
        if shifr == suz:
            print('Siz yutdingiz')
            break
    else:
        print('Harf topilmadi')
        ochko -= 1
        print('Sizda {} ta ochko qoldi'.format(ochko))
        if ochko == 0:
            print('Siz yutqazdingiz')
            break
