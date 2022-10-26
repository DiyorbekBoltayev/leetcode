sonlar=[]
for xayr in range(100,1000):
   if xayr > 1:
       for i in range(2, xayr):
           if (xayr % i) == 0:
               break
       else:
           sonlar.append(xayr)
for bye in sonlar:
    bye+=2
    if bye in sonlar:
        print(bye-2,bye)

