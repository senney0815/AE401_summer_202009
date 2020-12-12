from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

ans=randrange(16)

while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        hit>hits[5]
        block=mc.getBlockWithData(hit.pos)
        color=block.data
        
        if color>ans:
            mc.postToChat('太大了')
        elif color<ans:
            mc.postToChat('太小了')
        else:
            #答對了
            mc.postToChat('答對了')
            mc.setBlock(hit.pos.x,hit.pos.y,hit.pos.z,57)
            break
            #次數超過五次
            mc.postToChat('次數用完了')
            break
            
            