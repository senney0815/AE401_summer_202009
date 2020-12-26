from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

name=input('請問你的名字是？')

l=input(name+'請問你的的房子要蓋多長？')
w=input(name+'請問你的房子要蓋多寬？')
h=input(name+'請問你的房子要蓋多高？')

blockID=input(name+'請問你的建材要用什麼ID？')

l=int(l)
w=int(w)
h=int(h)
blockID=int(blockID)

mc.setBlocks(x,y,z,x+l,y+h,z+w,blockID)
mc.setBlocks(x+1,y+1,z+1,x+l-1,y+h-1,z+w-1,0)

mc.postToChat(name+'，你用的建材是ID'+str(blockID))
mc.postToChat('房子的尺寸是：'+str(l)+'X'+str(w)+'X'+str(h))
