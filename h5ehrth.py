import pygame 
import sys 
import random 

pygame.init() 
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Pygame Sample") 
font = pygame.font.Font(None, 36) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
r = RED 
center = (750, 50) 
image = pygame.image.load(r"c:\Users\user\Pictures\GOPR0148.JPG") 
image = pygame.transform.scale(image, (100, 50))
image2 = pygame.image.load(r"c:\Users\user\Pictures\GOPR0148.JPG") 
image2 = pygame.transform.scale(image2, (50, 50))
square_size = 50 
square_x = (screen_width - square_size) // 2 
square_y = (screen_height - square_size) 
speed = 5 
k = 2 
z = 3 
Objekt2 = 0 
y = 0 
Objekt3 = "" 
s = random.randint(50, 700) 
running = True 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: 
        square_x -= speed 
    if keys[pygame.K_RIGHT]: 
        square_x += speed 

    screen.fill(WHITE) 
    y += k 
    if y <= 600.0 and y >= 550.0: 
        y = 0 
        z -= 1
        Objekt2 -= 1
        if Objekt2 == 2 or Objekt2 == 5 or Objekt2 == 8 or Objekt2 == 11:
            k -= 1 
            s = random.randint(50, 700)
        if Objekt2 == -1:
            Objekt2 = 0
        s = random.randint(50, 700) 
    elif s <= square_x + 50 and s >= square_x - 50 and y >= square_y - 50 and y <= square_y + 50: 
        y = 0 
        s = random.randint(50, 700) 
        Objekt2 += 1 
        if Objekt2 == 3 or Objekt2 == 6 or Objekt2 == 9 or Objekt2 == 12 or Objekt2 == 15: 
            k += 1 

    text = font.render(f"{Objekt2}", True, r) 
    text_rect = text.get_rect(center=(750, 50)) 
    screen.blit(text, text_rect) 

    text = font.render(f"{z}", True, r) 
    text_rect = text.get_rect(center=(50, 50)) 
    screen.blit(text, text_rect) 
    if Objekt3 != "Вы выиграли" and Objekt3 != "Вы проиграли":
        screen.blit(image, (square_x, square_y)) 
        screen.blit(image2, (s, y)) 

    text = font.render(f"{Objekt3}", True, r) 
    text_rect = text.get_rect(center=(400, 300)) 
    screen.blit(text, text_rect)

    if Objekt2 == 5: 
        k = 0 
        Objekt2 = ""
        z = ""
        r = (0, 0, 0) 
        Objekt3 = "Вы выиграли" 
    elif z == 0: 
        k = 0 
        Objekt2 = ""
        z = ""
        r = (0, 0, 0) 
        Objekt3 = "Вы проиграли" 

    pygame.display.flip() 
    pygame.time.Clock().tick(60)  

pygame.quit() 
sys.exit()