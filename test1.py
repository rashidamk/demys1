import operator
A = {'A':'1,2,3','B':'4,6','C':'1,4,6','D':'5,2,8'}
mod = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'8':0}
for b in A.values():
   for i in mod.keys():
       mod[i]=mod[i]+b.count(i)
print(mod)
sorted_mod = sorted(mod.items(), key=operator.itemgetter(1),reverse=True)
i=0
B = set()
M = set()
C=A
while(i<len(sorted_mod)):
    for b in A.items():
        if(sorted_mod[i][0] in b[1]):
            B=B|{b[0]}
            del A[b[0]]
    print(B)
    M=M|{sorted_mod[i][0]}
    if(len(A) is 0):
       break;
    i=i+1
print(M)

        

