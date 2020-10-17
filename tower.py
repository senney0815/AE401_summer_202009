from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.setBlocks(
        x+50,y-1,z+50,
        x-50,y-1,z-50,47)
