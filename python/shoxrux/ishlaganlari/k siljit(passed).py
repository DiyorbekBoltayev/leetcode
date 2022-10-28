a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',' ',' ',' ',' ',' ',' ',' ',' ',' ','.','.','.','.','.','.','.','.','.','.']
b=input()
k=int(input())
l=[]
for i in b:
    d=a.index(i)
    l.append(a[d+k])
for i in l:
	print(i,end='')