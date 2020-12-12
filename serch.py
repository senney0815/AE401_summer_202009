from time import time
from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ans=randrange(100000001)

def LinearSerch():
    startTime=time()
    for i in range(100000001):
        if i==ans:
            print('答案是'+str(i))
            print('跑了'+str(time()-startTime))
            break
            
def BinearySerch():
    startTime=time()
    lower=0
    upper=100000000
    
    while lower<=upper:
        mid=(lower+upper)//2
        
        if ans<mid:
            upper=mid-1
        elif ans>mid:
            lower=mid+1
        else:
            print('答案是'+str(mid))
            print('跑了'+str(time()-startTime))
            break
        
LinearSerch()
BinearySerch()