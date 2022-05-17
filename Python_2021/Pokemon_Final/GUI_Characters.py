import pygame
from os import path
import pickle
import math
import random

pygame.font.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color, width, height, name, file):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.name = name
        self.width = width
        self.height = height
        self.image = pygame.image.load(file)
        # self.image.fill(color)

        self.rect = self.image.get_rect()
        # self.rect.center = (width / 2, height / 2)
    
    def check_clicked(self):
        # flags for mouse position on the object
        x_check = False
        y_check = False
        pos_list = pygame.mouse.get_pos()
        # \/ used to debug and check coordinates
        # print(pos_list)
        # checks if the mouse position upon clicking is within the boundaries of the object
        if pos_list[0] < self.rect.x + self.width and pos_list[0] > self.rect.x:
            x_check = True
        if pos_list[1] < self.rect.y + self.height and pos_list[1] > self.rect.y:
            y_check = True
        if x_check == True and y_check == True:
            # print(self.name)
            return True
        else:
            return False
    
    def test_attack(self, power, accuracy):
        # default values
        critical = 1
        damage = 0
        status_update = ''

        # if hit doesn't land, return miss
        # accuracy is given by the move requesting an attack
        hit_roll = random.randint(1, accuracy)
        if hit_roll == 1:
            status_update = 'MISS'
            return damage, status_update

        # check for 1 in 10 change critical hit (deals 1.5x damage)
        crit_roll = random.randint(1, 10)
        if crit_roll == 1:
            critical = 1.5
            status_update = 'CRIT'
        else:
            status_update = 'HIT'

        # provides randomness to the damage calculation so each roll is slightly different
        variance = float(format(random.uniform(0.8, 1.2), '.3f'))

        # calculates damage and rounds to nearest int
        damage = math.ceil(power * variance * critical)
        return [damage, status_update]
    
    def try_flee(self):
        # roll for flee
        flee_roll = random.randint(1, 2)
        # print(flee_roll)
        if flee_roll == 1:
            return 'FLEE'
        else:
            return 'FAIL'

class Erased(pygame.sprite.Sprite):
    def __init__(self, color, width, height, name):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        # self.rect.center = (width / 2, height / 2)

# class for character (and hpbar) sprites
class Character(pygame.sprite.Sprite):
    def __init__(self, index):
        pygame.sprite.Sprite.__init__(self)

        # reads the .dat file according to the passed index
        data_file = open('data/' + str(index) + '.dat', 'rb')
        # character_dict = {}
        character_dict = pickle.load(data_file)

        # loads sprite to a variable before attritube
        sprite = pygame.image.load('assets/' + character_dict['filename'])

        self.name = character_dict['name']
        self.health = character_dict['health']
        self.max_health = character_dict['health']
        self.power = character_dict['power']
        self.image = sprite
        self.rect = self.image.get_rect()

    # puts enemy in the correct spot
    def enemy_position(self):
        self.image = pygame.transform.scale(self.image, [512, 512])
        self.rect.x = 440
        self.rect.y = -60

    # 'sets' a character's health value after taking damage
    def health_update(self, damage):
        result = self.health - damage
        if result <= 0:
            self.health = 0
        else:
            self.health = result
    
    def heal(self):
        result = self.health + 10
        if result > self.max_health:
            self.health = self.max_health
        else:
            self.health = result

    # puts character in the correct spot
    def character_position(self):
        self.image = pygame.transform.scale(self.image, [512, 512])
        self.rect.x = 40
        self.rect.y = 150
    
# class for text objects
class Text():
    def __init__(self, text, x_pos, y_pos, size):

        # gets font and rectangular coordinates
        self.font = pygame.font.Font('assets/fonts/kongtext.ttf', size)
        self.text_surface = self.font.render(text, False, (0, 0, 0))
        self.x = x_pos
        self.y = y_pos
    
    # changes text attribute to what is passed
    def update_text(self, new_text, size):
        self.font = pygame.font.Font('assets/fonts/kongtext.ttf', size)
        self.text_surface = self.font.render(new_text, False, (0, 0, 0))
        return

    # changes position of the text object
    def update_position(self, x, y):
        self.x = x
        self.y = y

    # getter for the text surface
    def get_text_surface(self):
        return self.text_surface
    