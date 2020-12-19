from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    posts=mc.events.pollChatPosts()
    if len(posts)>0:
        post=posts[0]
        p=str(post)
        mc.postToChat(p)
        
        comma1=p.find(',')
        comma2=p.find(',',comma1+1)
        
        eID=int(p[comma1+1:comma2])
        
        x,y,z=mc.entity.getTilePos(eID)
        name=mc.entity.getName(eID)
        words=p[comma2+1:len(p)-1]
        
        mc.setSign(x,y,z,63,0,name,'',words)
        
        