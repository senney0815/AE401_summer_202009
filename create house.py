from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

length=30
width=30
height=20

block=57
air=0

mc.setBlocks(x,y,z,x+length,y+height,z+width,block)

mc.setBlocks(x,y,z,x+length-1,y+height-1,z+width-1,air)
