while True:
    b=input()
    f=[]
    r=1
    for i in b:
        f.append(i)
    for i in range(len(b)+1):
        if len(b)==i+1:
                break
        else:
            if f[i]<f[i+1]:
                r+=1
            else: 
                print(f[i+1])
    if r==len(b):
        print(True)
        