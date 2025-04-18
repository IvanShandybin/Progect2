import pygame,sys
pygame.init()
SCREEN_WIDTH=1800
SCREEN_HEIGHT=1000
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
CELL_SIZE=50
view_x=0
view_y=0
MOVE_SPEED=10
clock=pygame.time.Clock()
pole=[[0 for _ in range(SCREEN_HEIGHT//CELL_SIZE)] for _ in range(SCREEN_WIDTH//CELL_SIZE)]
zvetlast=0
Objekt=None
running=True
images={
    1:pygame.transform.scale(pygame.image.load('1.png'), (50,50)),
    2:pygame.transform.scale(pygame.image.load('2.png'), (50,50)),
    3:pygame.transform.scale(pygame.image.load('3.png'), (50,50)),
    4:pygame.transform.scale(pygame.image.load('4.png'), (50,50)),
    5:pygame.transform.scale(pygame.image.load('5.png'), (50,50)),
    6:pygame.transform.scale(pygame.image.load('6.png'), (50,50)), 
    7:pygame.transform.scale(pygame.image.load('7.png'), (50,50)), 
    8:pygame.transform.scale(pygame.image.load('8.png'), (50,50)),
    9:pygame.transform.scale(pygame.image.load('9.png'), (50,50)), 
    10:pygame.transform.scale(pygame.image.load('10.png'), (50,50)),
}
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            zvetlast=zvetlast+1
            if zvetlast==11:
                zvetlast=0
            cell_x = (event.pos[0] + view_x) // CELL_SIZE
            cell_y = (event.pos[1] + view_y) // CELL_SIZE
            if 0 <= cell_x < len(pole) and 0 <= cell_y < len(pole[0]):
                pole[cell_x][cell_y] = zvetlast
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            zvetlast=zvetlast-1
            if zvetlast==-1:
                zvetlast=10
            cell_x = (event.pos[0] + view_x) // CELL_SIZE
            cell_y = (event.pos[1] + view_y) // CELL_SIZE
            if 0 <= cell_x < len(pole) and 0 <= cell_y < len(pole[0]):
                pole[cell_x][cell_y] = zvetlast
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        view_x-=MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        view_x+=MOVE_SPEED
    if keys[pygame.K_UP]:
        view_y-=MOVE_SPEED
    if keys[pygame.K_DOWN]:
        view_y+=MOVE_SPEED
    if view_x<0:
        view_x+=MOVE_SPEED
    if view_y<0:
        view_y+=MOVE_SPEED
    screen.fill(WHITE)
    start_x=view_x//CELL_SIZE
    start_y=view_y//CELL_SIZE
    end_x=(view_x+SCREEN_WIDTH)//CELL_SIZE+1
    end_y=(view_y+SCREEN_HEIGHT)//CELL_SIZE+1
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            screen_x=i*CELL_SIZE-view_x
            screen_y=j*CELL_SIZE-view_y
            pygame.draw.rect(screen,BLACK,(screen_x,screen_y,CELL_SIZE,CELL_SIZE),1)
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if pole[i][j]!=0:
                screen_x=i*CELL_SIZE-view_x
                screen_y =j*CELL_SIZE-view_y
                screen.blit(images[pole[i][j]],(screen_x,screen_y))
    if Objekt is not None:
        font=pygame.font.Font(None, 36)
        text=font.render(Objekt,True,BLACK)
        screen.blit(text,(10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
