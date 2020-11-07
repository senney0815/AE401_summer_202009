from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
         hit=hits[0]
         x,y,z=hit.pos
         block=mc.getBlock(x,y,z)
         
         mc.postToChat('受虐的方塊是：'+str(block))