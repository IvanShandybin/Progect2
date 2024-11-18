import pygame, sys

pygame.init()
width=int(input())
height=int(input())
size=100
a=(0,0,0)
b=(255,255,255)
disp=pygame.display.set_mode((width+800,height))
Objekt=None
font = pygame.font.Font(None, 36)
Paravila="1-Минотавр 2-Ключ 3-Выход 4-Начало реки 5-Конец реки"
Paravila2="6-Река 7-Стена 8-Портал 9-Больница 0-Начало"
### Задание поля #############################################################################################
pole=[]
for i in range(width//size):
    pole.append([0]*(height//size))
print(pole)
while True:
###### Закрытие программы #####################################################################################
    for c in pygame.event.get():
        if c.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
###############################################################################################################
######## Проверка последней нажатой цифры #####################################################################
        if c.type==pygame.KEYDOWN:
            if c.key==pygame.K_1:
                Objekt="Минотавр"
            elif c.key==pygame.K_2:
                Objekt= "Ключ "
            elif c.key==pygame.K_3:
                Objekt= "Выход"
            elif c.key==pygame.K_4:
                Objekt="Начало Реки"
            elif c.key==pygame.K_5:
                Objekt="Конец Реки"
            elif c.key==pygame.K_6:
                Objekt="Река"
            elif c.key==pygame.K_7:
                Objekt="Стена"
            elif c.key==pygame.K_8:
                Objekt="Портал"
            elif c.key==pygame.K_9:
                Objekt="Больница"
            elif c.key==pygame.K_0:
                Objekt= "Начало"
###############################################################################################################
###############################################################################################################
    disp.fill(b)
    for row in range(height//size):
        for col in range(width//size):
            pygame.draw.rect(disp,a,(col*size,row*size,size,size),1)
    if Objekt is not None:
        text=font.render(Objekt,True,a)
        text_rect=text.get_rect(center=(width+100,height//2))
        disp.blit(text,text_rect)
    text=font.render(Paravila,True,a)
    text_rect=text.get_rect(center=(width+400,height-250))
    disp.blit(text,text_rect)
    text=font.render(Paravila2,True,a)
    text_rect=text.get_rect(center=(width+400,height-200))
    disp.blit(text,text_rect)
    pygame.display.flip()
############################################################################################################