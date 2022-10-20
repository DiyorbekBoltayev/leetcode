
def onoltilik_sakkizlik(a):
    return oct(a)
a = input('16 lik sanoq sistemasidagi sonni kiriting: ')
print('sonni sakkizlik sanoq sistemasiga o\'tkazildi: ')
print(onoltilik_sakkizlik(int(a, 16))[2:])
