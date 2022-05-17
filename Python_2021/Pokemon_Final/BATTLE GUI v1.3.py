from cgitb import text
import pygame
import random
import math
import time
from os import path
from GUI_Characters import Character
from GUI_Characters import Text

pygame.font.init()
pygame.init()
pygame.display.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)
BLACK = (0, 0, 0)

class Button(pygame.sprite.Sprite):
    def __init__(self, color, width, height, name):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
    
    def check_clicked(self):
        # flags for mouse position on the object
        x_check = False
        y_check = False
        pos_list = pygame.mouse.get_pos()
        print(pos_list)
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
        

def battle_start():
    # load window and clock
    screen = pygame.display.set_mode((900, 720))
    pygame.display.set_caption("Sprite test")
    clock = pygame.time.Clock()

    won = False

    # background
    background = pygame.image.load('background.png')
    screen.blit(background, (0, 0))
    
    # tracks the current game operation
    NextGameState = 'IDLE'

    # spawns button objects
    Attack = Button(BLUE, 280, 100, 'attack')
    Items = Button(RED, 280, 100, 'items')
    Flee = Button(GREEN, 280, 100,  'flee')

    # Attack position
    Attack.rect.x = 18
    Attack.rect.y = 610

    # Items Position
    Items.rect.x = 308
    Items.rect.y = 610

    # Flee Position
    Flee.rect.x = 598
    Flee.rect.y = 610

    # creates and adds buttons to group
    active_buttons = pygame.sprite.Group()
    active_buttons.add(Attack)
    active_buttons.add(Items)
    active_buttons.add(Flee)

    # eraser group
    Eraser = Button(WHITE, 880, 50, 'eraser')
    Eraser.rect.x = 10
    Eraser.rect.y = 545
    eraser_group = pygame.sprite.Group()

    # hp bars
    health_bar1 = Character('hp bar', 1, pygame.image.load('hpbar.png'))
    health_bar2 = Character('hp bar', 1, pygame.image.load('hpbar.png'))
    health_bar1.rect.x = 339
    health_bar1.rect.y = 157
    health_bar2.rect.x = 455
    health_bar2.rect.y = 356

    hp_group = pygame.sprite.Group()

    hp_group.add(health_bar1)
    hp_group.add(health_bar2)

    # draw hp bars
    hp_group.update()
    hp_group.draw(screen)

    # load enemy object and sprite
    enemy_sprite = pygame.image.load('dunsparce.png')
    Enemy = Character('Enemy', 50, enemy_sprite)

    Enemy.enemy_position()
    active_characters = pygame.sprite.Group()
    active_characters.add(Enemy)

    # enemy health default
    enenmy_hp_text = Text(str(Enemy.health) + '/' + str(Enemy.max_health) + ' HP', 352, 181, 24)
    screen.blit(enenmy_hp_text.get_text_surface(), (enenmy_hp_text.x, enenmy_hp_text.y))

    # load character object and sprite
    dunsparce_sprite = pygame.image.load('dunsparce_back.png')
    dunsparce = Character('Dunsparce', 51, dunsparce_sprite)
    dunsparce.character_position()
    active_characters.add(dunsparce)

    # character health default
    character_hp_text = Text(str(dunsparce.health) + '/' + str(dunsparce.max_health) + ' HP', 468, 381, 24)
    screen.blit(character_hp_text.get_text_surface(), (character_hp_text.x, character_hp_text.y))
    
    # main text default
    text_object = Text('A wild Dunsparce appeared!', 80, 560, 30)
    screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))

    running = True
    while running:
        clock.tick(60)
        
        # check for win flag
        if won == True:
            time.sleep(4)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Attack.check_clicked() == True:
                    NextGameState = 'ATTACK'
                if Items.check_clicked() == True:
                    NextGameState = 'ITEMS'
                if Flee.check_clicked() == True:
                    NextGameState = 'FLEE'
        
        if Enemy.health <= 0:
            # you beat him!
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # add win text
            text_object.update_text('You won the battle!', 30)
            text_object.update_position(175,560)
            screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))

            won = True

        
        if NextGameState == 'ATTACK':
            # erases old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # stores result as a list
            result = Attack.test_attack(5, 8)

            # result -> display result text and subtract health.
            if result[1] == 'MISS':
                text_object.update_text('You missed!', 30)
                text_object.update_position(290,560)
                screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))
            if result[1] == 'CRIT':
                # changes main text
                text_object.update_text('Critical Hit! ' + str(result[0]) + ' Damage dealt', 27)
                text_object.update_position(70,563)
                screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))

                # changes health text (enemy took damage)
                hp_group.draw(screen)
                Enemy.health_update(result[0])
                enenmy_hp_text.update_text(str(Enemy.health) + '/' + str(Enemy.max_health) + ' HP', 24)
                screen.blit(enenmy_hp_text.get_text_surface(), (enenmy_hp_text.x, enenmy_hp_text.y))

                # reprint character text too...
                screen.blit(character_hp_text.get_text_surface(), (character_hp_text.x, character_hp_text.y))

            if result[1] == 'HIT':
                text_object.update_text('Hit! ' + str(result[0]) + ' Damage dealt', 30)
                text_object.update_position(160,560)
                screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))

                # changes health text (enemy took damage)
                hp_group.draw(screen)
                Enemy.health_update(result[0])
                enenmy_hp_text.update_text(str(Enemy.health) + '/' + str(Enemy.max_health) + ' HP', 24)
                screen.blit(enenmy_hp_text.get_text_surface(), (enenmy_hp_text.x, enenmy_hp_text.y))

                # reprint character text too...
                screen.blit(character_hp_text.get_text_surface(), (character_hp_text.x, character_hp_text.y))
                

            NextGameState = 'IDLE'

        
        # print(clock)
        # screen.fill(BLACK)
        active_characters.update()
        active_characters.draw(screen)
        active_buttons.update()
        active_buttons.draw(screen)
        pygame.display.flip()


battle_start()