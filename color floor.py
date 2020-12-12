from random import  randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(20):
    x,y,z=mc.player.getTilePos()
    x=x+i
    
    for j in range(20):
        color=randrange(16)
        z=z+1
        mc.setBlock(x,y,z,35,color)