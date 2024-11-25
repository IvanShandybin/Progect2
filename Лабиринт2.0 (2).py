import pygame,sys
pygame.init()
width=int(input())
height=int(input())
size=100
m=True
a=(0,0,0)
b=(255,255,255)
disp=pygame.display.set_mode((1800,1000))
Objekt=None
zvetlast=0
zvet=[]
r=0
x=[]
y=[]
r=0
font = pygame.font.Font(None, 36)
Cnopkagotovo="ГОЙДА"
Paravila="1-Минотавр 2-Ключ 3-Выход 4-Начало реки 5-Конец реки"
Paravila2="6-Река 7-Стена 8-Портал 9-Больница 0-Начало"
### Задание поля #############################################################################################
pole=[]
for i in range(width//size):
    pole.append([0]*(height//size))
while m==True:
###### Закрытие программы #####################################################################################
    for c in pygame.event.get():
        if c.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
###############################################################################################################
#######Отслеживание нажатие мыши###############################################################################
        elif c.type == pygame.MOUSEBUTTONDOWN and c.button == 1:
            if(1100<c.pos[0]<1300 and 650<c.pos[1]<750):
                    m=False
            if c.pos[0]<width and c.pos[1]<height and zvetlast!=0:
                r=1
                x.append(c.pos[0])
                y.append(c.pos[1])
                zvet.append(zvetlast)
                pole[(c.pos[1]//100)][(c.pos[0]//100)]=zvetlast
###############################################################################################################
######## Проверка последней нажатой цифры #####################################################################
        if c.type==pygame.KEYDOWN:
            if c.key==pygame.K_1:
                zvetlast=1
                Objekt="Минотавр"
            elif c.key==pygame.K_2:
                zvetlast=2
                Objekt= "Ключ"
            elif c.key==pygame.K_3:
                zvetlast=3
                Objekt= "Выход"
            elif c.key==pygame.K_4:
                zvetlast=4
                Objekt="Начало Реки"
            elif c.key==pygame.K_5:
                zvetlast=5
                Objekt="Конец Реки"
            elif c.key==pygame.K_6:
                zvetlast=6
                Objekt="Река"
            elif c.key==pygame.K_7:
                zvetlast=7
                Objekt="Стена"
            elif c.key==pygame.K_8:
                zvetlast=8
                Objekt="Портал"
            elif c.key==pygame.K_9:
                zvetlast=9
                Objekt="Больница"
            elif c.key==pygame.K_0:
                zvetlast=10
                Objekt= "Начало"
###############################################################################################################
#########Отрисовка#############################################################################################
    disp.fill(b)
    for row in range(height//size):
        for col in range(width//size):
            pygame.draw.rect(disp,a,(col*size,row*size,size,size),1)
    for i in range(len(x)):
        if zvetlast!=0 and r!=0:
            pygame.draw.rect(disp, (20*zvet[i], 10*zvet[i], 4*zvet[i]), (x[i]//100*100,y[i]//100*100, size, size), 100)
    if Objekt is not None:
        text=font.render(Objekt,True,a)
        text_rect=text.get_rect(center=(1300,500))
        disp.blit(text,text_rect)
    text=font.render(Paravila,True,a)
    text_rect=text.get_rect(center=(1300,550))
    disp.blit(text,text_rect)
    text=font.render(Paravila2,True,a)
    text_rect=text.get_rect(center=(1300,600))
    disp.blit(text,text_rect)
    text=font.render(Cnopkagotovo,True,a)
    text_rect=text.get_rect(center=(1300,700))
    disp.blit(text,text_rect)
    pygame.display.flip()
############################################################################################################
