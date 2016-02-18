import itertools
A = {'A':'1,2,3','B':'1,6','C':'2,4,6','D':'1,2,8'}
mod = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'8':0}
stuff = mod.keys()
def myfunc():
    M=set();
    min=100
    flag=0
    for L in range(0, len(stuff)+1):
      for subset in itertools.combinations(stuff, L):
        if(flag is 1):
            if(len(subset) > min):
                return
        i=0
        B=dict(A)
        while(i<len(subset)):
              for b in B.items():
                  if(subset[i] in b[1]):
                    del B[b[0]]
                
              i=i+1
        if(len(B) is 0):
            flag=1
            if(len(subset)<=min):
                min=len(subset)
                print(subset)
myfunc()
   
        
          

          
                  
