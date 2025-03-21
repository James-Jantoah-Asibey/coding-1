
import pygame
import random

# Initialize pygame
pygame.init()

display_width = 800 
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Moving Game object')

clock = pygame.time.Clock()

playerImg = pygame.image.load('player_image.png')

player_width = playerImg.get_width()
player_height = playerImg.get_height()

x = display_width // 2 - player_width // 2
y = display_height // 2 - player_height // 2
speed = 5

def player(x, y):
    gameDisplay.blit(playerImg, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            running = False

    keys = pygame.key.get_prpessed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed 

    if x < 0:
        x = 0
    if x > display_width - player_width:
        x = display_width - player_width
    if y < 0:
        y = 0
    if y > display_height - player_height:
        y = display_height - player_height

    gameDisplay.fill((255, 255, 255))

    player(x, y)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
     