from random import choice
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

def Play():
    symbol=['黑桃','紅心','方塊','梅花']
    number=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
   
    player1=[]
    player2=[]

    for i in range(3):
        
        player1.append(choice(symbol)+choice(number))
        player2.append(choice(symbol)+choice(number))
       
    mc.setSign(x,y,z,63,0,'玩家一抽到的是：',player1[0],player1[1],player1[2])
    mc.setSign(x+1,y,z,63,0,'玩家二抽到的是：',player2[0],player2[1],player2[2])
    
r=input('準備好了嗎(Y/N)？')
if r=='Y':
    Play()
else:
    print('準備好在來吧。')