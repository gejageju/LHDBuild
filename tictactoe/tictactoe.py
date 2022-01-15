import pygame
import math
import os

#setting up game window
pygame.init()
WIDTH,HEIGHT=800,700
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#colours
white=(255,255,255)
grey=(54,69,79)
BLACK=(0,0,0)

#game variables
points=[]
run=True
count=0
status=list(i*0 for i in range(0,16))
game=False
draw=False
total_press=0

#text
title=pygame.font.Font("norm.ttf",70)
Title=title.render("Tic Tac Toe",True,white)
text=pygame.font.Font("norm.ttf",100)
Turn=pygame.font.Font("norm.ttf",60)


#images
joystick=pygame.image.load("controller.png")
img= pygame.transform.smoothscale(joystick, (150,200))
x=pygame.image.load("cancel.png")
x=pygame.transform.smoothscale(x,(55,55))
y=pygame.image.load("o.png")
y=pygame.transform.smoothscale(y,(55,55))

if (not draw):

        win.fill(grey)
        win.blit(Title,(270,10))
        grid_size=450
        start_x=((WIDTH-grid_size)/2)
        start_y=((HEIGHT-grid_size)/3)
        gap=grid_size/3
        for i in range(0,16):
            points.append((start_x + (gap * (i % 4)), start_y + (gap * (i // 4))))

        for i in range(0,4):
              pygame.draw.line(win, white, points[i], points[i + 12], 3)
              pygame.draw.line(win, white, points[i * 4], points[i * 4 + 3], 3)
        win.blit(img,(0,0))
        pygame.display.flip()
        pygame.display.update()
def draw_text(str):
   if not draw:
    win.fill(BLACK)
    Text = text.render("PLAYER "+str+" WON", True, white)
    win.blit(Text, (100, 100))
    pygame.display.update()
def draw_window():
    draw=True
    win.fill(BLACK)
    Text=text.render("GAME DRAW",True,white)
    win.blit(Text,(100,100))
    pygame.display.update()
    print(draw)

def game_won(num):
  if (not draw):
    winner="X"if(status[num]==1)else"O"
    draw_text(winner)

def check_status(count,i):
    key=[0,1,2,4,5,6,8,9,10]
    var=1 if count%2==0 else 2
    status.pop(i)
    status.insert(i,var)
    print(status)
    print(total_press)
    if (total_press>=8)and(game==False):
        draw_window()
    else:
     for i in [0,1,2]:

        if(((status[i*4]==status[i*4+1]==status[i*4+2]!=0)or(status[i] == status[i+4] == status[i+8]!=0))):
                 game=True
                 game_won(i)
                 break
        if(((status[0] == status[5] == status[10])or(status[2] == status[5] == status[8]!=0))and status[5]!=0):
            game=True
            game_won(5)
            break

def draw_symbol(count,num):
 print(draw)
 if(not draw):
    if(count%2==0):
        var=x
        t="O"
    else:
          var=y
          t="x"
    win.blit(var,(points[num][0]+50,points[num][1]+50))
    pygame.display.update()


#game loop
while(run):

    for event in pygame.event.get():
       if event.type==pygame.QUIT:
          pygame.quit()
       if not draw:
        if event.type==pygame.MOUSEBUTTONDOWN:
           mx,my=pygame.mouse.get_pos()

           for i in range(0,16):
               if(((mx>points[i][0])and(mx<points[i+1][0]))and((my>points[i][1])and(my<points[i+4][1]))):
                   count+=1
                   draw_symbol(count,i)
                   check_status(count,i)
                   total_press+=1
               else: pass



