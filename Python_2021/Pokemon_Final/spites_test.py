

from turtle import down
import pygame

from test_config import *
from BATTLE_GUI_TESTING_SCENE import Button, battle_start
import test 

import math
import random


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

        


class PLAYER(pygame.sprite.Sprite):           # basics started by devin
    # class started by devin, (game allows access to main game, x and y are the x and y coordinates)
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # controlls the layer the player is on
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # these handle the screen size and width(devin)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # these valyes handle the storage and movement of the player(devin)
        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)  # the image of the player

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # basic code started by devin, just passes the above values to the main game
    def update(self):
        self.movement()
        self.animate()  # calls animate function to constantly update
        

        self.rect.x += self.x_change

        self.collide_blocks('x')
        

        self.rect.y += self.y_change

        self.collide_blocks('y')


        self.x_change = 0
        self.y_change = 0

    def movement(self):  # started by devin          controlls movement of the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    # detects collision between just blocks (DEVIN)
    def collide_blocks(self, direction):

        # these two functions handle collision detection for blocks object
        if direction == "x":
            # determines if the player is hitting a block
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    
                    
    def collide_grass(self, direction):
        hits_grass = pygame.sprite.spritecollide(self, self.game.grass, False)

        if direction == "x":
            
                # determines if the player is hitting a block
        
            if hits_grass:
                if self.x_change > 0:
                    while hits_grass:
                        for s in self.clock.tick(5):
                            print("money")                 
                if self.x_change < 0:
                    print("")        
        
        hits = pygame.sprite.spritecollide(self, self.game.grass, False)
        if direction == "y":
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


    def animate(self):
        pass
        #     # first sprite in list is idle, everything after is apart of the animation
        # down_animations = [self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""", self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""", 
        #     self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #     self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #     self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #     ]


        # up_animations = [self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""", 
        #                 self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                 self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                 ]

        # left_animations = [self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                     self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                     self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                     ]

        # right_animations = [self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                             self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                             self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""",
        #                             ]

        # if self.facing == "down": # idle animation
        #     if self.y_change == 0:
        #         self.image = self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""" # idle animation 
            
        #     else:   # walking down and up animations
        #         self.image = down_animations[math.floor(self.animation_loop)]  # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
        #         self.animation_loop += 0.1
        #         if self.animation_loop >= 3:
        #             self.animation_loop = 1

 
        # if self.facing == "up": # idle animation
        #     if self.y_change == 0:
        #         self.image = self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""" # idle animation 
            
        #     else:   # walking down and up animations
        #         self.image = up_animations[math.floor(self.animation_loop)]  # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
        #         self.animation_loop += 0.1
        #         if self.animation_loop >= 3:
        #             self.animation_loop = 1

        # if self.facing == "right": # idle animation
        #     if self.x_change == 0:
        #         self.image = self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""" # idle animation 
            
        #     else:   # walking down and up animations
        #         self.image = right_animations[math.floor(self.animation_loop)]  # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
        #         self.animation_loop += 0.1
        #         if self.animation_loop >= 3:
        #             self.animation_loop = 1


        # if self.facing == "left": # idle animation
        #     if self.x_change == 0:
        #         self.image = self.game.character_spritesheet.get_sprite"""(x, x, self.width, self.height)]""" # idle animation 
            
        #     else:   # walking down and up animations
        #         self.image = left_animations[math.floor(self.animation_loop)]  # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
        #         self.animation_loop += 0.1
        #         if self.animation_loop >= 3:
        #             self.animation_loop = 1

 
                 


        # if direction == "x":                # detects collision for grass, but allowing the player to pass through
        #     # determines if the player is touching grass
        #     hits = pygame.sprite.spritecollide(self, self.game.grass, False)
        #     if hits:
                # print("test")

                

        #         # if self.x_change > 0:
        #         #     pri
        #         # if self.x_change < 0:
        #         #         self.rect.x = hits[0].rect.right

        #     if direction == "y":
        #         hits = pygame.sprite.spritecollide(self, self.game.grass, False)
        #         if hits:
        #             self.p = self.p.battle_start()    
        # # started by devin, handles blocks on map and collison
                      


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER       # privatises the layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(449, 472, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



# started by devin, handles blocks on map and collison
class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = GRASS_LAYER       # privatises the layer
        self.groups = self.game.all_sprites, self.game.grass
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(
            37, 818, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


# (devin)- this is the bottom most layer of the level, appearing as the background for everything
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = GROUND_LAYER       # privatises the layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(
            400, 269, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
