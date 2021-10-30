import pygame
from PIL import Image

#initilise pygame
pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Shushi Maker 1')

#background
background = pygame.image.load('./python02/sushi_photo/sushi_02.jpg')
#images
shushi_table = pygame.image.load('./python02/sushi_photo/shushi_table.png')
bad_shushi_1 = pygame.image.load('./python02/sushi_photo/bad_shushi.png')
good_shushi = pygame.image.load('./python02/sushi_photo/Shushi_good.png')

#game loop
run = True
while run:
    #background image
    screen.blit(background, (0,0))

    #shushi_table image
    shushi_table = pygame.transform.scale(shushi_table, (345 * 2, 150 * 2))
    screen.blit(shushi_table, (80,350))
    screen.blit(bad_shushi_1, (300,450))
    screen.blit(good_shushi, (400, 450))
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()