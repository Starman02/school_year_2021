"""
Resources Used:
Sources and other help used:
-bits of help from Stack overflow
https://www.pygame.org/docs/ref/display.html
-some help from w3 schools
lots of help starting out with and organization help and general learning how pygame basics work from: https://www.youtube.com/playlist?list=PLkkm3wcQHjT7gn81Wn-e78cAyhwBW3FIc
help with doing the sleep parts of encounters https://realpython.com/python-sleep/ 
some help from the textbook.
"""

import pygame

from main_sprites import *

from config import *

import tkinter
import sys


class MainGame:  # started by devin
    def __init__(self):  # class started by devin
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = SpriteSheet('img/Wario_sprite_purple_fina.png')

        self.terrain_spritesheet = SpriteSheet("img/terrain.png")

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    PLAYER(self, j, i)
                if column == "G":
                    Grass(self, j, i)

    def new(self):  # devin-starts main game and tracks whethere the game is running

        self.playing = True

        # entire group of sprites(devin)
        self.all_sprites = pygame.sprite.LayeredUpdates()

        # blocks for collision and boundary (devin)
        self.blocks = pygame.sprite.LayeredUpdates()

        # blocks for collision and boundary (devin)
        self.grass = pygame.sprite.LayeredUpdates()

        self.createTileMap()

    def events(self):  # will handle events such as encounters (started by devn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def update(self):  # started by devin

        # constantly updates the game

        self.all_sprites.update()

    def draw(self):  # started by devin
        # controls the actual game screen
        self.all_sprites.draw(self.screen)

        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # main game loop, plays while game is running (started by devin)
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False


g = MainGame()
g.new()
# g.battle_attack()
while g.running:
    g.main()

pygame.quit()
sys.exit()
