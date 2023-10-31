import pygame
import sys

pygame.init()
global r
global h
global f
global s
r=0
h=0
f=0
s=0
resolution = (1280,780)
screen=pygame.display.set_mode(resolution)
pygame.display.set_caption('RUN | HIDE | FIGHT | STEAL')
class Event:
    def __init__(event,text,n,png):
        background=(15,23,63)
        global r
        global h
        global f
        global s
        event.n=n
        event.text=text
        ui=pygame.image.load('assets/ui.PNG').convert_alpha()
        screen.blit(ui,(0,0))
        event.screen=png
   
        text=font.render(event.text,True,textColor)
        screen.blit(text,(width-1195,height-320))
    
        screen.blit(event.screen,(70,65))

        if ev.type ==pygame.MOUSEBUTTONDOWN:
            #run button
            if 80 <= mouse[0] <= 300 and 620 <= mouse [1] <= 700:
                r=event.n     
                h=0
                f=0
                s=0
                print(2)
            #hide button         
            elif 380 <= mouse[0] <= 600 and 620 <= mouse [1] <= 700:
                
                h=event.n        
                r=0
                f=0
                s=0
            #fight button   
            elif 680 <= mouse[0] <= 900 and 620 <= mouse [1] <= 700:
            
                f=event.n    
                r=0
                h=0
                s=0
            #steal button         
            elif 980 <= mouse[0] <= 1200 and 620 <= mouse [1] <= 700:
            
                s=event.n
                r=0
                f=0
                r=0
r=0
h=0
f=0
s=0
        
textColor=(53,76,76)
width=screen.get_width()
height=screen.get_height()
 

font=pygame.font.SysFont('Arial', 30)
while True:
    
    for ev in pygame.event.get():

        
        if ev.type == pygame.QUIT:
            pygame.quit()
            
        
        if r<=2 and h<=2 and f<=2 and s<=2:
            if r==0 and h==0 and f==0 and s==0:
                start=Event("",1,pygame.image.load('assets/Title.png').convert_alpha())
            elif r==1 or h==1 or f==1 or s==1:
                x1=Event("You wake up in a forest with no memory and a bag of gold coins. What do you do?",2,pygame.image.load('assets/forest1.png').convert_alpha())
            elif r==2:
                r1=Event("You run through the forest and reach a clearing. There is a bridge up ahead. What do you do?",3,pygame.image.load('assets/field.png').convert_alpha())
            elif h==2:
                h1=Event("You hide in the bushes. An angry man appears from the trail, holding a weapon. What do you do?",4,pygame.image.load('assets/thief.png').convert_alpha())
            elif f==2:
                f1=Event("You fight the air. In your struggle, someone appears from behind you and stabs you. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==2:
                s1=Event("You steal some leaves from a nearby tree. It gets mad at you. What do you do?",5,pygame.image.load('assets/treemad.png').convert_alpha())
        elif r<=4 and h<=4 and f<=4 and s<=4:
            if r==3:
                r2=Event("You run towards the bridge. Something appears to be chuckling underneath it. What do you do?",6,pygame.image.load('assets/bridge.png').convert_alpha())
            elif h==3:
                h2=Event("You hide in the bushes. Nothing Happens. What do you do?",3,pygame.image.load('assets/field.png').convert_alpha())
            elif f==3:
                f2=Event("You fight the concept of a clearing. It takes 2 damage. What do you do?",7,pygame.image.load('assets/field fight.png').convert_alpha())
            elif s==3:
                s2=Event("You steal the grass from a section of the field. The ground is exposed. What do you do?",8,pygame.image.load('assets/field dirt.png').convert_alpha())
            elif r==4:
                r3=Event("You jump out of the bushes and try to run away. The man stabs you. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==4:
                h3=Event("You stay in the bushes. A robed individual and a goblin appear behind the man. What do you do?",9,pygame.image.load('assets/forest thief crew.png').convert_alpha())
            elif f==4:
                f3=Event("You hop out of the bushes and punch him in the gut. He curls over in pain. What do you do?",10,pygame.image.load('assets/thief hurt.png').convert_alpha())
            elif s==4:
                s3=Event("You rustle the bushes. The man walks over. You steal his weapon. He sees you. What do you do?",11,pygame.image.load('assets/thief yikes.png').convert_alpha())
        elif r<=6 and h<=6 and f<=6 and s<=6:
            if r==5:
                r4=Event("You run from the tree, but the forest is filled with its friends. You are now dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==5:
                h4=Event("You hide in the bushes. The tree is now confused. What do you do?",12,pygame.image.load('assets/treehuh.png').convert_alpha())
            elif f==5:
                f4=Event("You fight the tree, but it's dumb to hit a tree. The tree gets even more angry. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==5:
                s4=Event("You steal the tree's arms. The tree can't hit you. What do you do?",13,pygame.image.load('assets/tree no arms.png').convert_alpha())
            elif r==6:
                r5=Event("A troll jumps in front of you, saying \"He He He! Give three coins to me!\" What do you do?",14,pygame.image.load('assets/bridge troll.png').convert_alpha())
            elif h==6:
                h5=Event("You hide in the bushes. The chuckling stops. What do you do?",6,pygame.image.load('assets/bridge.png').convert_alpha())
            elif f==6:
                f5=Event("You fight the bridge. It breaks, exposing a startled troll. What do you do?",15,pygame.image.load('assets/bridge break.png').convert_alpha())
            elif s==6:
                s5=Event("You steal the bridge. A few planks fall off and a startled troll is exposed. What do you do?",15,pygame.image.load('assets/bridge break.png').convert_alpha())
        elif r<=8 and h<=8 and f<=8 and s<=8:
            if r==7:
                r6=Event("You try to outrun the concept of a field, but you can't outrun an idea. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==7:
                h6=Event("You try to hide from the concept of a field. It finds its way into your mind. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==7:
                f6=Event("You kill the concept of a field and reality breaks. You are dead but also not. Who's to say?",0,pygame.image.load('assets/game break.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            elif s==7:
                s6=Event("You steal the concept of a field. The game has no purpose now.",0,pygame.image.load('assets/blank.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            elif r==8:
                r7=Event("You run towards the bridge. Something appears to be chuckling underneath it. What do you do?",6,pygame.image.load('assets/bridge.png').convert_alpha())
            elif h==8:
                h7=Event("You hide in the bushes. The exposed earth gives off a menacing aura. What do you do?",8,pygame.image.load('assets/field dirt.png').convert_alpha())
            elif f==8:
                f7=Event("You punch the exposed earth. Nothing happens. Try stealing the dirt.",8,pygame.image.load('assets/field dirt.png').convert_alpha())
            elif s==8:
                s7=Event("You steal some dirt. A hole is formed. What do you do?",16,pygame.image.load('assets/field hole.png').convert_alpha())
        elif r<=10 and h<=10 and f<=10 and s<=10:
            if r==9:
                r8=Event("You jump out of the bushes & try to make a run for it. The group kills you & takes their gold back.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==9:
                h8=Event("You hide in the bushes. The heroes start looking around. What do you do?",17,pygame.image.load('assets/forest thief crew.png').convert_alpha())
            elif f==9:
                f8=Event("You jump out of the bushes and try fighting the group. You are pulverized.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==9:
                s8=Event("You steal the robed individual's orb. The orb pulses with energy. What do you do?",18,pygame.image.load('assets/uh oh.png').convert_alpha())
            elif r==10:
                r9=Event("You run away from the man and straight into his associates. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==10:
                h9=Event("You hide in the bushes, and a robed individual and a goblin help the man to his feet. What do you do?",9,pygame.image.load('assets/forest thief crew.png').convert_alpha())
            elif f==10:
                f9=Event("You kick the man again, but the man's friends find you and obliterate you. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==10:
                s9=Event("You steal the man's valuables. His friends show up and aren't happy. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
        elif r<=12 and h<=12 and f<=12 and s<=12:
            if r==11:
                r10=Event("You run away from the man and straight into his associates. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==11:
                h10=Event("You hide in a bush. A goblin and robed individual join the man and search for you. What do you do?",19,pygame.image.load('assets/forest thief crew2.png').convert_alpha())
            elif f==11:
                f10=Event("You jump out of the bushes and try fighting the man. You kill him, but his associates find you. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==11:
                s10=Event("You steal the man's clothes. The ESRB provide a barrel to keep the game rated E. What do you do?",20,pygame.image.load('assets/barrelman.png').convert_alpha())
            elif r==12:
                r11=Event("You jump out of the bushes and run, but the forest is filled with the tree's friends. You are now dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==12:
                h11=Event("You stay in the bushes. The tree is still confused. What do you do?",12,pygame.image.load('assets/treehuh.png').convert_alpha())
            elif f==12:
                f11=Event("You jump out and fight the tree, but the element of surprise didn't work. The tree gets even more angry. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==12:
                s11=Event("You jump out and steal the tree's arms. The tree can't hit you. What do you do?",13,pygame.image.load('assets/tree no arms.png').convert_alpha())
        elif r<=14 and h<=14 and f<=14 and s<=14:
            if r==13:
                r12=Event("You run straight into the tree. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==13:
                h12=Event("You hide in a bush. The Tree just stares at you. What do you do?",13,pygame.image.load('assets/tree sad.png').convert_alpha())
            elif f==13:
                f12=Event("You fight the tree and win. The path is clear. What do you do?",21,pygame.image.load('assets/tree stump.png').convert_alpha())
            elif s==13:
                s12=Event("You steal the tree. The path is clear. What do you do?",21,pygame.image.load('assets/forest1.png').convert_alpha())
            elif r==14:
                r13=Event("You try to run past the troll. \"My toll has not been paid. 3 coins for the way!\"",22,pygame.image.load('assets/bridge troll.png').convert_alpha())
            elif h==14:
                h13=Event("You hide in a bush. The troll is confused. What do you do?",22,pygame.image.load('assets/bridge troll confused.png').convert_alpha())
            elif f==14:
                f13=Event("You fight the troll, who smashes your head in with his bag of coins. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==14:
                s13=Event("You steal the bag of coins. \"My coins, you knave, my coins! Give them back or I'll kick your loins!\"",23,pygame.image.load('assets/bridge troll mad.png').convert_alpha())
        elif r<=16 and h<=16 and f<=16 and s<=16:
            if r==15:
                r14=Event("You run to the river. The troll says \"Hello, My friend, hello! Where'd my house happen to go?\"",24,pygame.image.load('assets/troll river.png').convert_alpha())
            elif h==15:
                h14=Event("You hide in the bushes. The troll blinks and looks around. What do you do?",15,pygame.image.load('assets/bridge break.png').convert_alpha())
            elif f==15:
                f14=Event("You fight the air. The troll watches from the river. What do you do?",15,pygame.image.load('assets/bridge break.png').convert_alpha())
            elif s==15:
                s14=Event("There is nothing left to steal.",15,pygame.image.load('assets/bridge break.png').convert_alpha())
            elif r==16:
                r15=Event("You run into the hole and fall headfirst a great distance. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==16:
                h15=Event("You hide in the bushes. The hole caves in, and you fall in and die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==16:
                f15=Event("You try to punch the hole, but punching an empty space doesn't seem to do much.",16,pygame.image.load('assets/field hole.png').convert_alpha())
            elif s==16:
                s15=Event("You try to dig more, but fall in by mistake. The hole is deeper than you thought. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
        elif r<=18 and h<=18 and f<=18 and s<=18:
            if r==17:
                r16=Event("You jump out of the bushes & try to make a run for it. The group kills you & takes their gold back.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==17:
                h16=Event("The group find you and kill you.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==17:
                f16=Event("You jump out of the bushes and try fighting the group. You are pulverized.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==17:
                s16=Event("You steal the robed individual's orb. The orb pulses with energy. What do you do?",18,pygame.image.load('assets/uh oh.png').convert_alpha())
            elif r==18:
                r17=Event("You try to run away, but the goblin stabs you. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==18:
                h17=Event("You try to hide, but the orb's glow is very apparent. You are killed.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==18:
                f17=Event("You smash the orb on the ground. You and everyone in a 5-mile radius die in the resulting explosion.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==18:
                s17=Event("You steal the orb's magic. You *Ascend.* You are no longer bound by four options.",26,pygame.image.load('assets/stars.png').convert_alpha())
        elif r<=20 and h<=20 and f<=20 and s<=20:
            if r==19:
                r18=Event("You jump out of the bushes & try to make a run for it. The group kills you & takes their gold back.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==19:
                h18=Event("The group start looking for you. What do you do?",25,pygame.image.load('assets/forest thief crew2.png').convert_alpha())
            elif f==19:
                f18=Event("You jump out of the bushes and try fighting the group. Despite your weapon, you are pulverized.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==19:
                s18=Event("You steal the robed individual's orb. The orb pulses with energy. What do you do?",17,pygame.image.load('assets/uh oh 2.png').convert_alpha())
            elif r==20:
                r19=Event("You jump out of the bushes & try to make a run for it. The group kills you & takes their stuff back.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==20:
                h19=Event("You try to hide, but you've given away your location. You are killed.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==20:
                f19=Event("You try to stab the man, but the barrel blocks the weapon. His group show up and kill you.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==20:
                s19=Event("You steal the barrel. The game is shut down by the ESRB.",0,pygame.image.load('assets/blank.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
        elif r<=22 and h<=22 and f<=22 and s<=22:
            if r==21:
                r20=Event("You run through the forest and reach a clearing. There is a bridge up ahead. What do you do?",3,pygame.image.load('assets/field.png').convert_alpha())
            elif h==21:
                h20=Event("You hide in the bushes. An angry man appears from the trail, holding a weapon. What do you do?",4,pygame.image.load('assets/forest thief.png').convert_alpha())
            elif f==21:
                f20=Event("You try fighting the air. The friends of the tree you killed get their revenge. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==21:
                s20=Event("You steal some leaves from another tree. It gets mad at you. What do you do?",5,pygame.image.load('assets/treemad.png').convert_alpha())
            elif r==22:
                r21=Event("You try to run past the troll again. It's losing its patience. \"3 coins is the price. I'm trying to be nice.\"",27,pygame.image.load('assets/bridge troll pushy 1.png').convert_alpha())
            elif h==22:
                h21=Event("You hide in the bushes. \"You know I see you, right? There are no other bushes in sight.\"",27,pygame.image.load('assets/bridge troll confused.png').convert_alpha())
            elif f==22:
                f21=Event("You fight the troll, who smashes your head in with his bag of coins. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==22:
                s21=Event("You steal the bag of coins. \"My coins, you knave, my coins! Give them back or I'll kick your loins!\"",23,pygame.image.load('assets/bridge troll mad.png').convert_alpha())
        elif r<=24 and h<=24 and f<=24 and s<=24:
            if r==23:
                r22=Event("You try to run past the troll, but he kicks you in the crotch and beats you to death.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==23:
                h22=Event("You hide in the bushes. The troll is unphased and beats you to death.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==23:
                f22=Event("You fight the troll. It kicks you in the crotch and beats you to death.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==23:
                s22=Event("You try stealing from the troll again, but it kicks you in the crotch and beats you to death instead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif r==24:
                r23=Event("Run past the troll through the river. You are in an empty field. For some reason, you feel free.",0,pygame.image.load('assets/freedom.png').convert_alpha())
            elif h==24:
                h23=Event("You hide in the river. You drown.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==24:
                f23=Event("You fight the troll, who holds you under the water. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==24:
                s23=Event("You steal the troll's bag of coins. The troll holds you under the water. You die",0,pygame.image.load('assets/gameover.png').convert_alpha())
        elif r<=26 and h<=26 and f<=26 and s<=26:
            if r==25:
                r24=Event("You jump out of the bushes & try to make a run for it. The group kills you & takes their stuff back.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==25:
                h24=Event("The group find you and kill you.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==25:
                f24=Event("You jump out of the bushes and try fighting the group. You are pulverized.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==25:
                s24=Event("You steal the robed individual's orb. The orb pulses with energy. What do you do?",18,pygame.image.load('assets/uh oh 2.png').convert_alpha())
            elif r==26:
                r25=Event("wcuroiudshgckoiesxgkdcoismkgxo8ixrtlw09rk8zyl9x7rmcsuxmocrhsucormxw9s8mc9e8srlck89iocg9xospicluh8xy09cet y4wmc8tipw8t mxhpmwcmkux0rwexow7yx07g8w08s7cmhwmc8o8pwsk9rlya9htlsw9kl",0,pygame.image.load('assets/x.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            elif h==26:
                h25=Event("wucpm90ctrsdyf0kcw9es8mygc0w8erskerxngmc9ws08rxey9s7cg8xms7rgmxs798rym80wx9m7grw87cgrnw8ncxm9e8rymkw9s0kxc8rmks08mdcwc9ers8d7gjc8s7cn87rgyj8s7gyje8jscr7ensx7gys8djx7eygw8s7r8g",0,pygame.image.load('assets/x.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            elif f==26:
                f25=Event("w89xmtcrsd89regxm,rldg0l9escsdodhercgwcmr98so7wcnw87gcms8w7gm8w7yrs8ygdfgjcxkmvsomezeciespafcm8rsyevc89aedsufycw8rspcngvs9r8egms7ngns97kergiusovgsrmkogifsuhvgimoclxvsuov",0,pygame.image.load('assets/x.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
            elif s==26:
                s25=Event("womepdszocghdiushmgiouce98rw9c4t98ewrscmwsk9des8tfjde87snyv0cmrde98dm0tcew9r8c7tw8ekr9s8tck9ed7yg09zpcgm0rv9cukufed9symer8c7s8rmcgy7s9fykcudvn8nwfj8dk9e0r8tye79tr0s8cmr",0,pygame.image.load('assets/x.png').convert_alpha())
                if ev.type ==pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
        elif r<=28 and h<=28 and f<=28 and s<=28:
            if r==27:
                r26=Event("You try to run again. The troll isn't having it. \"Dude, just pay the toll. If you don't I'll get fired.\"",28,pygame.image.load('assets/bridge troll pushy 2.png').convert_alpha())
            elif h==27:
                h26=Event("You hide in the bushes. \"You're hiding isn't helping anyone. Just Pay.\"",28,pygame.image.load('assets/bridge troll pushy 2.png').convert_alpha())
            elif f==27:
                f26=Event("You fight the troll, who smashes your head in with his bag of coins. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==27:
                s26=Event("You steal the bag of coins. \"My coins, you knave, my coins! Give them back or I'll kick your loins!\"",23,pygame.image.load('assets/bridge troll mad.png').convert_alpha())
            elif r==28:
                r27=Event("You try to run past again. The troll is enraged. \"JUST GIVE ME THE COINS!\"",29,pygame.image.load('assets/troll guy pushy3.png').convert_alpha())
            elif h==28:
                h27=Event("You hide in the bushes. The troll is enraged. \"STOP HIDING IN THOSE BUSHES AND PAY UP!\"",29,pygame.image.load('assets/troll guy pushy3.png').convert_alpha())
            elif f==28:
                f27=Event("You fight the troll, who smashes your head in with his bag of coins. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==28:
                s27=Event("You steal the bag of coins. \"My coins, you knave, my coins! Give them back or I'll kick your loins!\"",23,pygame.image.load('assets/bridge troll mad.png').convert_alpha())
        elif r<=30 and h<=30 and f<=30 and s<=30:
            if r==29:
                r28=Event("You try to run past again. The troll pushes you over the bridge. You die.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif h==29:
                h28=Event("You hide in the bushes. The troll takes his bag of coins and flattens your hiding spot. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif f==29:
                f28=Event("You fight the troll, who smashes your head in with his bag of coins. You are dead.",0,pygame.image.load('assets/gameover.png').convert_alpha())
            elif s==29:
                s28=Event("You steal the bag of coins. \"My coins, you knave, my coins! Give them back or I'll kick your loins!\"",23,pygame.image.load('assets/bridge troll mad.png').convert_alpha())
           


    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    