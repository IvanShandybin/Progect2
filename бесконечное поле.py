import pygame
import sys
pygame.init()
SCREEN_WIDTH=1800
SCREEN_HEIGHT=1000
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
CELL_SIZE=50
view_x=0
view_y=0
MOVE_SPEED=10
clock=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        view_x-=MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        view_x+=MOVE_SPEED
    if keys[pygame.K_UP]:
        view_y-=MOVE_SPEED
    if keys[pygame.K_DOWN]:
        view_y+=MOVE_SPEED
    screen.fill(WHITE)
    start_x=view_x//CELL_SIZE
    start_y=view_y//CELL_SIZE
    end_x=(view_x+SCREEN_WIDTH)//CELL_SIZE+1
    end_y=(view_y+SCREEN_HEIGHT)//CELL_SIZE+1
    for i in range(start_x,end_x):
        for j in range(start_y,end_y):
            screen_x=i*CELL_SIZE-view_x
            screen_y=j*CELL_SIZE-view_y
            pygame.draw.rect(screen,BLACK,(screen_x,screen_y,CELL_SIZE,CELL_SIZE),1)
            if i==0 and j==0:
                pygame.draw.rect(screen,RED,(screen_x,screen_y,CELL_SIZE,CELL_SIZE))
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
sys.exit()
