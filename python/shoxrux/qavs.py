a=input()
ochildi=0
yopildi=0
ans=True
for i in range(len(a)):
    if a[i]=="(":
        ochildi+=1
    elif a[i]==")":
        yopildi+=1
    if(yopildi>ochildi):
        ans=False
        break
if ochildi != yopildi:
    ans=False

if ans:
    print('Tog\'ri')
else:
    print("Xato")
