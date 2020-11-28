from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

n=1

for i in range(8):
    
    for j in range(n):
        mc.spawnEntity(x,y,z,60)
        
    n=n*2
    
    mc.postToChat('這次生成了'+str(n)+'隻囊蟲')
    