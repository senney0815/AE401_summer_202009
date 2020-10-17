from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat(
            "you are loctted on x:"+str(x)+",y:"+str(y)+",z:"+str(z))