n=int(input("n="))
soni60=0
soni10=0
soni1=0
count60=n//60;
count10=n//10;
holatlar=[]
# 1 sayohat 15  ; 10-sayohat 125; 60 sayohat 440
for i in range(0,count60+2):
    for j in range(0,count10+2):
        for k in range(0,10):
            if i*60+j*10+k >=n:
                holatlar.append([i,j,k])
pullar=holatlar.copy()

for i in range(0,len(holatlar)):
    pullar[i]=holatlar[i][0]*440+holatlar[i][1]*125+holatlar[i][2]*15

print(holatlar[pullar.index(min(pullar))])


