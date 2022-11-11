n=int(input("n="))
soni60=0
soni10=0
soni1=0
count60=n//60;
count20=n//20;
count10=n//10;
count5=n//5;
count1=int(str(n)[-1])
holatlar=[]
# 1 sayohat 15  ; 5 sayohat 70; 10-sayohat 125;20 sayohat 230; 60 sayohat 440
for i in range(0,count60+2):
    for j in range(0,count20+2):
        for k in range(0,count10+2):
            for l in range(0,count5+2):
                for m in range(0,count1+2):
                    if i*60+j*20+k*10+l*5+m >=n:
                        holatlar.append([i,j,k,l,m])
                        
pullar=holatlar.copy()
for i in range(0,len(holatlar)):
    pullar[i]=holatlar[i][0]*440+holatlar[i][1]*230+holatlar[i][2]*125+holatlar[i][3]*70+holatlar[i][4]*15



print(holatlar[pullar.index(min(pullar))])


