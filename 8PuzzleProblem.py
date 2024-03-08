D={(1,2,3,4,5,6,7,8,0):0}
E=D.copy()

def Z(a,d):
    b=list(a)
    b[i],b[i+d]=b[i+d],0
    b=tuple(b)
    if b not in E:
        E[b]=a
        D[b]=D[a]+1

for x in range(32):
    for a in E.copy():
        i=list(a).index(0)
        if i>2:
            Z(a,-3)
        if i%3:
            Z(a,-1)
        if i%3<2:
            Z(a,1)
        if i<6:
            Z(a,3)

g=[]
for x in range(3):
    g+=map(int,input().split())

g=tuple(g)
if g in E:
 print(D[g])
 while g:
    for i in (0,3,6):
        print('%d %d %d'%g[i:i+3])
    g=E[g]
    print()
else:
    print( -1)
