import pygame,sys,subprocess,threading,os
pygame.init()
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None
filename="ads.py"
file_path=find_file(filename, os.getcwd())
images={
    1:pygame.transform.scale(pygame.image.load('1.png'), (100, 100)),
    2:pygame.transform.scale(pygame.image.load('2.png'), (100, 100)),
    3:pygame.transform.scale(pygame.image.load('3.png'), (100, 100)),
    4:pygame.transform.scale(pygame.image.load('4.png'), (100, 100)),
    5:pygame.transform.scale(pygame.image.load('5.png'), (100, 100)),
    6:pygame.transform.scale(pygame.image.load('6.png'), (100, 100)), 
    7:pygame.transform.scale(pygame.image.load('7.png'), (100, 100)), 
    8:pygame.transform.scale(pygame.image.load('8.png'), (100, 100)),
    9:pygame.transform.scale(pygame.image.load('9.png'), (100, 100)), 
    10:pygame.transform.scale(pygame.image.load('10.png'), (100, 100)),
}
def proverka(xn,yn):
    if pole[yn][xn]==1:
        Objekt3="Минотавр"
    elif pole[yn][xn]==0:
        Objekt3="Пустая клетка"
    elif pole[yn][xn]==2:
        Objekt3="Ключ"
    elif pole[yn][xn]==3:
        Objekt3="Выход"
    elif pole[yn][xn]==4:
        Objekt3="Начало Реки"
    elif pole[yn][xn]==5:
        Objekt3="Конец Реки"
    elif pole[yn][xn]==6:
        Objekt3="Река"
    elif pole[yn][xn]==7:
        Objekt3="Стена"
    elif pole[yn][xn]==8:
        Objekt3="Портал"
    elif pole[yn][xn]==9:
        Objekt3="Больница"
    elif pole[yn][xn]==10:
        Objekt3="Начало"
    return Objekt3
def run_infinite_field():
    subprocess.run([sys.executable,file_path])
def reca(xn,yn):
        for h in range(len(rekax)):
            if xn==rekax[h] and yn==rekay[h]:
                nom=h
        if naprav[nom]==1:
            yn=yn-1
        elif naprav[nom]==2:
            yn=yn+1
        elif naprav[nom]==3:
            xn=xn-1
        elif naprav[nom]==4:
            xn=xn+1
        return xn,yn
size=100
Objekt2="Вы стоите в начале"
Objekt3="Путую клетку"
xn=-1
yn=-1
xb=0
yb=0
nom=0
countb=0
kluch=0
nu=0
m=False
Igrok2=False
a=(0,0,0)
b=(255,255,255)
disp=pygame.display.set_mode((1800,1000))
Objekt=None
zvetlast=0
zvet=[]
r=0
x=[]
y=[]
portx=[]
porty=[]
rekax=[]
rekay=[]
naprav=[]
napravi=0
font=pygame.font.Font(None,36)
Cnopkagotovo="ГОЙДА"
Paravila="1-Минотавр 2-Ключ 3-Выход 4-Начало реки 5-Конец реки"
Paravila2="6-Река 7-Стена 8-Портал 9-Больница 0-Начало"
Vbor="Введите размеры поля от 5 до 9"
g=True
pole=[]
razmer1=0
razmer2=0
width=500
height=500
wi=0
while g==True:
    for c in pygame.event.get():
        if c.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif c.type == pygame.MOUSEBUTTONDOWN and c.button == 1:
            if(700<c.pos[0]<1100 and 850<c.pos[1]<950):
                    m=True
                    g=False
        elif c.type==pygame.KEYDOWN:
            if wi==0:
                if c.key==pygame.K_5:
                    width=500
                    wi=1
                elif c.key==pygame.K_6:
                    width=600
                    wi=1
                elif c.key==pygame.K_7:
                    width=700
                    wi=1
                elif c.key==pygame.K_8:
                    width=800
                    wi=1
                elif c.key==pygame.K_9:
                    width=900
                    wi=1
            else:
                if c.key==pygame.K_5:
                    height=500
                elif c.key==pygame.K_6:
                    height=600
                elif c.key==pygame.K_7:
                    height=700
                elif c.key==pygame.K_8:
                    height=800
                elif c.key==pygame.K_9:
                    height=900
            if c.key==pygame.K_BACKSPACE:
                wi=0
    Vborw=f"{width//100}x{height//100}"
    disp.fill(b)
    text=font.render(Vborw,True,a)
    text_rect=text.get_rect(center=(900,700))
    disp.blit(text,text_rect)
    text=font.render(Vbor,True,a)
    text_rect=text.get_rect(center=(900,500))
    disp.blit(text,text_rect)
    text=font.render(Cnopkagotovo,True,a)
    text_rect=text.get_rect(center=(900,900))
    disp.blit(text,text_rect)
    pygame.display.flip()
### Задание поля #############################################################################################
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
                    Igrok2=True
            if c.pos[0]<width and c.pos[1]<height and zvetlast!=0:
                r=1
                x.append(c.pos[0])
                y.append(c.pos[1])
                zvet.append(zvetlast)
                pole[(c.pos[1]//100)][(c.pos[0]//100)]=zvetlast
                if zvetlast==10 and xn==-1 and yn==-1:
                    xn=c.pos[0]//100
                    yn=c.pos[1]//100
                elif zvetlast==9 and countb==0:
                    xb=c.pos[0]//100
                    yb=c.pos[1]//100
                    countb=1
                elif zvetlast==2:
                    nu=nu+1
                elif zvetlast==8:
                    portx.append(c.pos[0]//100)
                    porty.append(c.pos[1]//100)
                elif zvetlast==4:
                    rekax.append(c.pos[0]//100)
                    rekay.append(c.pos[1]//100)
                    napravi=1
                    while napravi==1:
                        for k in pygame.event.get():
                            if k.type==pygame.KEYDOWN:
                                if k.key==pygame.K_UP:
                                   naprav.append(1)
                                   napravi=0
                                elif k.key==pygame.K_DOWN:
                                   naprav.append(2)
                                   napravi=0
                                elif k.key==pygame.K_LEFT:
                                    naprav.append(3)
                                    napravi=0
                                elif k.key==pygame.K_RIGHT:
                                    naprav.append(4)
                                    napravi=0
                elif zvetlast==6:
                    rekax.append(c.pos[0]//100)
                    rekay.append(c.pos[1]//100)
                    napravi=1
                    while napravi==1:
                        for k in pygame.event.get():
                            if k.type==pygame.KEYDOWN:
                                if k.key==pygame.K_UP:
                                   naprav.append(1)
                                   napravi=0
                                elif k.key==pygame.K_DOWN:
                                   naprav.append(2)
                                   napravi=0
                                elif k.key==pygame.K_LEFT:
                                    naprav.append(3)
                                    napravi=0
                                elif k.key==pygame.K_RIGHT:
                                    naprav.append(4)
                                    napravi=0
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
            disp.blit(images[zvet[i]],(x[i]//100*100,y[i]//100*100))
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
pole2=[]
for i in range(width//size):
    pole2.append([0]*(height//size))
while Igrok2==True:
    disp.fill(b)
    for c in pygame.event.get():
        if c.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if c.type == pygame.MOUSEBUTTONDOWN and c.button == 1:
            if(1100<c.pos[0]<1300 and 650<c.pos[1]<850):
                threading.Thread(target=run_infinite_field).start()
        if c.type==pygame.KEYDOWN:
            if c.key==pygame.K_UP:   
                yn=yn-1  
                if yn<0:
                    Objekt3="Стена"
                else:
                    Objekt3=proverka(xn,yn)
                Objekt2=f"Вы сдвинулись на клетку вверх и встретили {Objekt3}"
                if Objekt3=="Стена":
                    yn=yn+1
                elif Objekt3=="Минотавр":
                    yn=yb
                    xn=xb
                elif Objekt3=="Ключ":
                    kluch=kluch+1
                    pole[yn][xn]=0
                elif Objekt3=="Выход" and kluch==nu:
                    Objekt2="Вы победили!"
                elif Objekt3=="Портал":
                    for h in range(len(portx)):
                        if xn==portx[h] and yn==porty[h]:
                            nom=h
                            nom=nom+1
                        if nom==len(portx):
                            nom=0
                    xn=portx[nom]
                    yn=porty[nom]
                elif Objekt3=="Начало Реки":
                   xn,yn=reca(xn,yn)
                elif Objekt3=="Река":
                    xn,yn=reca(xn,yn)
            elif c.key==pygame.K_DOWN:
                yn=yn+1
                if yn==height//100:
                    Objekt3="Стена"
                else:
                    Objekt3=proverka(xn,yn)
                Objekt2=f"Вы сдвинулись на клетку вниз и встретили {Objekt3}"
                if Objekt3=="Стена":
                    yn=yn-1
                elif Objekt3=="Минотавр":
                    yn=yb
                    xn=xb
                elif Objekt3=="Ключ":
                    kluch=kluch+1
                    pole[yn][xn]=0
                elif Objekt3=="Выход" and kluch==nu:
                    Objekt2="Вы победили!"
                elif Objekt3=="Портал":
                    for h in range(len(portx)):
                        if xn==portx[h] and yn==porty[h]:
                            nom=h
                            nom=nom+1
                        if nom==len(portx):
                            nom=0
                    xn=portx[nom]
                    yn=porty[nom]
                elif Objekt3=="Начало Реки":
                    xn,yn=reca(xn,yn)
                elif Objekt3=="Река":
                    xn,yn=reca(xn,yn)
            elif c.key==pygame.K_LEFT:
                xn=xn-1
                if xn<0:
                    Objekt3="Стена"
                else:
                    Objekt3=proverka(xn,yn)
                Objekt2=f"Вы сдвинулись на клетку влево и встретили {Objekt3}"
                if Objekt3=="Стена":
                    xn=xn+1
                elif Objekt3=="Минотавр":
                    yn=yb
                    xn=xb
                elif Objekt3=="Ключ":
                    kluch=kluch+1
                    pole[yn][xn]=0
                elif Objekt3=="Выход" and kluch==nu:
                    Objekt2="Вы победили!"
                elif Objekt3=="Портал":
                    for h in range(len(portx)):
                        if xn==portx[h] and yn==porty[h]:
                            nom=h
                            nom=nom+1
                        if nom==len(portx):
                            nom=0
                    xn=portx[nom]
                    yn=porty[nom]
                elif Objekt3=="Начало Реки":
                    xn,yn=reca(xn,yn)
                elif Objekt3=="Река":
                    xn,yn=reca(xn,yn)
            elif c.key==pygame.K_RIGHT:
                xn=xn+1
                if xn==width//100:
                    Objekt3="Стена"
                else:
                    Objekt3=proverka(xn,yn)
                Objekt2=f"Вы сдвинулись на клетку вправо и встретили {Objekt3}"
                if Objekt3=="Стена":
                    xn=xn-1
                elif Objekt3=="Минотавр":
                    yn=yb
                    xn=xb
                elif Objekt3=="Ключ":
                    kluch=kluch+1
                    pole[yn][xn]=0
                elif Objekt3=="Выход" and kluch==nu:
                    Objekt2="Вы победили!"
                elif Objekt3=="Портал":
                    for h in range(len(portx)):
                        if xn==portx[h] and yn==porty[h]:
                            nom=h
                            nom=nom+1
                        if nom==len(portx):
                            nom=0
                    xn=portx[nom]
                    yn=porty[nom]
                elif Objekt3=="Начало Реки":
                    xn,yn=reca(xn,yn)
                elif Objekt3=="Река":
                    xn,yn=reca(xn,yn)
    text=font.render(Objekt2,True,a)
    text_rect=text.get_rect(center=(1300,500))
    disp.blit(text,text_rect)
    pygame.draw.rect(disp,a,(1100,650,200,200),1)
    print(yn)
    print(xn)
    pygame.display.flip()
    print(rekay)
    print(naprav)
    pygame.display.flip()
