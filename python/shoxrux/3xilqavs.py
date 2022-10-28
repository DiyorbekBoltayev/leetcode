ochilgan_qavslar = ["[", "{", "("]
yopilgan_qavslar = ["]", "}", ")"]
#()((())){[]}
#
def togri_qavsmi(satr):
    stek = []
    for i in satr:
        if i in ochilgan_qavslar:
            stek.append(i)
        elif i in yopilgan_qavslar:
            joylashuvi = yopilgan_qavslar.index(i)
            if ((len(stek) > 0) and
                    (ochilgan_qavslar[joylashuvi] == stek[-1])):
                stek.pop()
            else:
                return "YOQ"
    if len(stek) == 0:
        return "HA"
    else:
        return "YOQ"


qavslar = "{[]{(){}}}"
print(qavslar, "-", togri_qavsmi(qavslar))
