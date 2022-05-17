







import pygame



from test_config import *
#from BATTLE_GUI_TESTING_SCENE import *


import time

import math
import random


class SpriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite

    def get_sprite_black(self, x, y, width, height):
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

        self.image = self.game.character_spritesheet.get_sprite(
            3, 2, self.width, self.height)  # the image of the player

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # basic code started by devin, just passes the above values to the main game
    def update(self):
        self.movement()

        self.animate()  # calls animate function to constantly update

        self.rect.x += self.x_change

        self.collide('x')

        self.rect.y += self.y_change

        self.collide('y')

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
    def collide(self, direction):

        # these two functions handle collision detection for blocks object
        if direction == "x":
            # determines if the player is hitting a block
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hits_grass = pygame.sprite.spritecollide(
                self, self.game.grass, False)

            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

            if hits_grass:
                if self.x_change > 0:
                    time.sleep(5)

                    battle_start()
                if self.x_change < 0:
                    time.sleep(5)
                    
                    battle_start()
                    
                        
                


        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hits_grass = pygame.sprite.spritecollide(
                self, self.game.grass, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

                    # determines if the player is hitting a bloc
            if hits_grass:
                if self.y_change > 0:
                    time.sleep(5)
                    
                    battle_start()
                if self.y_change < 0:
                    time.sleep(5)
                   
                    battle_start()


        # #   # first sprite in list is idle, everyth fing after is apart of the animation

    def animate(self):

        down_animations = [self.game.character_spritesheet.get_sprite(3, 159, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               0, 79, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(29, 79, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 79, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(
                             0, 79, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(29, 79, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(2, 4, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               3, 158, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               36, 158, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(
                               69, 158, self.width, self.height)
                           ]

        right_animations = [self.game.character_spritesheet.get_sprite(2, 4, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(
                                3, 158, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(
                                36, 158, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(69, 158, self.width, self.height)]

        if self.facing == "down":  # idle animation
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    132, 198, self.width, self.height)  # idle animation

            else:   # walking down and up animations
                # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
                self.image = pygame.transform.flip(
                    down_animations[math.floor(self.animation_loop)], False, True)
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":  # idle animation
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    132, 198, self.width, self.height)  # idle animation

            else:   # walking down and up animations
                # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":  # idle animation
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    132, 198, self.width, self.height)  # idle animation

            else:   # walking down and up animations
                # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":  # idle animation
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(
                    132, 198, self.width, self.height)  # idle animation

            else:   # walking down and up animations
                # as Y is changing, every 10 frames the game will loop through animations 1 2 and 3, its 3 because of the current number of animations, the number will change based on the number of frames in the list
                self.image = pygame.transform.flip(
                    left_animations[math.floor(self.animation_loop)], True, False)
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


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

        self.image = self.game.terrain_spritesheet.get_sprite(
            449, 472, self.width, self.height)
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

        self.image = self.game.terrain_spritesheet.get_sprite_black(
            1, 813, self.width, self.height)

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
            411, 283, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
