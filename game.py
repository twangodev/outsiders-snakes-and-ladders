import pygame
import json

with open('config.json') as configuration: #Read JSON from config.json
    config = json.loads(configuration.read())

#Initialize pygame
pygame.init()

# Create Window
gameDisplay = pygame.display.set_mode((config["display"]["width"], config["display"]["height"]))
pygame.display.set_caption(config["display"]["caption"])