from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
         hit=hits[0]
         x,y,z=hit.pos
        
         mc.setBlock(x,y,z,41)
        