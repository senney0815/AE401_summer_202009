from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()
   #葉子18 #樹幹17
mc.setBlocks(x,y+3,z,x+2,y+3+2,z+2,18)
mc.setBlocks(x+1,y,z+1,x+1,y+4,z+1,17)



