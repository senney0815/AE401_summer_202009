from mcpi.minecraft import Minecraft
mc=Minecraft.create()
myId=mc.getPlayerEntityId('54Senney')
x,y,z=mc.entity.getTilePos(myId)

list2d=[[57,0,0,0,57],
        [57,0,0,0,57,57],
        [57,0,0,57,57,57],
        [57,0,0,0,0,57,57,57,57],
        [57,57,57,57,0,0,57],
        [57,0,0,0,57,57],
        [57,0,0,0,57,0,0,57],
        [57,0,57,57,57,0]]

startX=x

for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        x=x+1
    
    x=startX
    z=z+1