shoh1=input()
shoh1=shoh1.split()
bowqa1=input()
bowqa1=bowqa1.split()
if int(shoh1[0])-int(bowqa1[0])==int(shoh1[1])-int(bowqa1[1]):
    if int(shoh1[0])-int(bowqa1[0])==1 and int(shoh1[1])-int(bowqa1[1])==1:
        print(True)
elif  (shoh1[0]==bowqa1[0] or shoh1[1]==bowqa1[1]):
    if int(shoh1[0])>int(bowqa1[1]):
        if int(shoh1[0])-int(bowqa1[1]) >1:
            print(False)
