import pygame
import json
import time

with open('config.json') as configuration: #Read JSON from config.json
    config = json.loads(configuration.read())

#Initialize pygame
pygame.init()

# Create Window
gameDisplay = pygame.display.set_mode((config["display"]["width"], config["display"]["height"]))
pygame.display.set_caption(config["display"]["caption"])

#Load Images
startingbg = pygame.image.load("./assets/startingbg.png")
startbtn = pygame.image.load("./assets/startbtn.png")
grid = pygame.image.load("./assets/grid.png")

#Variables
clock = pygame.time.Clock()

def centercoord(imageh, imagew):
    centerscreencoord_height = config["display"]["height"]
    centerscreencoord_width = config["display"]["width"]
    x = (centerscreencoord_width/2)-(imagew/2)
    y = (centerscreencoord_height/2)-(imageh/2)
    return [int(x),int(y)]

def start():
    loop = True
    while(loop == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                print("Game Quit")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= centercoord(30,100)[0] and event.pos[0] <= (centercoord(30,100)[0]+100) and event.pos[1] >= centercoord(30,100)[1] and event.pos[1] <= (centercoord(30,100)[1]+30):
                    mainscreen()
                    loop = False
        gameDisplay.blit(startingbg, [0,0]) #Set Background
        gameDisplay.blit(startbtn, centercoord(30, 100))
        pygame.display.update()
        clock.tick(config["display"]["fps"])
        pygame.display.flip()

def mainscreen():
    loop = True
    while(loop == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                print("Game Quit")
        gameDisplay.blit(grid, [0,0]) #Set Background
        pygame.display.update()
        clock.tick(config["display"]["fps"])
        pygame.display.flip()

start()