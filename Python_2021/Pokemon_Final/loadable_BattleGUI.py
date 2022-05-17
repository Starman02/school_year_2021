from cgitb import text
import pygame
import random
import math
import time
# from os import path
from GUI_Characters import Text
from GUI_Characters import Character
from GUI_Characters import Erased
from GUI_Characters import Button

pygame.font.init()
pygame.init()
pygame.display.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def battle_start(C_INDEX, E_INDEX):
    # load window and clock
    screen = pygame.display.set_mode((900, 720), pygame.RESIZABLE)
    pygame.display.set_caption("Battle")
    clock = pygame.time.Clock()

    Fleed = False

    # background
    background = pygame.image.load('GUI_Assets/background.png')
    screen.blit(background, (0, 0))

    # tracks the current game operation
    NextGameState = 'IDLE'

    # spawns button objects
    Attack = Button(BLUE, 280, 100, 'attack', 'GUI_Assets/buttons/attack.png')
    Items = Button(RED, 280, 100, 'items', 'GUI_Assets/buttons/heal.png')
    Flee = Button(GREEN, 280, 100,  'flee', 'GUI_Assets/buttons/flee.png')

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
    Eraser = Erased(WHITE, 880, 50, 'eraser')
    Eraser.rect.x = 10
    Eraser.rect.y = 545
    eraser_group = pygame.sprite.Group()

    # hp bars
    health_bar1 = Character('hpbar')
    health_bar2 = Character('hpbar')
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
    # enemy_sprite = pygame.image.load('dunsparce.png')
    Enemy = Character(E_INDEX)

    Enemy.enemy_position()
    active_characters = pygame.sprite.Group()
    active_characters.add(Enemy)

    # enemy health default
    enenmy_hp_text = Text(str(Enemy.health) + '/' +
                          str(Enemy.max_health) + ' HP', 352, 181, 24)
    screen.blit(enenmy_hp_text.get_text_surface(),
                (enenmy_hp_text.x, enenmy_hp_text.y))

    # load character object and sprite
    # dunsparce_sprite = pygame.image.load('dunsparce_back.png')
    dunsparce = Character(C_INDEX)
    dunsparce.character_position()
    active_characters.add(dunsparce)

    # character health default
    character_hp_text = Text(
        str(dunsparce.health) + '/' + str(dunsparce.max_health) + ' HP', 468, 381, 24)
    screen.blit(character_hp_text.get_text_surface(),
                (character_hp_text.x, character_hp_text.y))

    # main text default
    text_object = Text('A wild ' + str(Enemy.name) + ' appeared!', 80, 560, 30)
    screen.blit(text_object.get_text_surface(), (text_object.x, text_object.y))

    running = True
    while running:
        clock.tick(60)
        # print(NextGameState)

        # check for win flag
        if NextGameState == 'WIN' or NextGameState == 'LOSE':
            time.sleep(3)
            running = False

        # check for flee flag
        if Fleed == True:
            time.sleep(3)
            running = False

        # look for event flags
        for event in pygame.event.get():
            # user closes the window
            if event.type == pygame.QUIT:
                running = False
            # user clicks anywhere on screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Attack.check_clicked() == True:
                    NextGameState = 'ATTACK'
                if Items.check_clicked() == True:
                    NextGameState = 'HEAL'
                if Flee.check_clicked() == True:
                    NextGameState = 'FLEE'

        if Enemy.health <= 0:
            # you beat him!
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # add win text
            text_object.update_text('You won the battle!', 30)
            text_object.update_position(175, 560)
            screen.blit(text_object.get_text_surface(),
                        (text_object.x, text_object.y))

            # flag a win for when the next frame is rendered
            NextGameState = 'WIN'

        if dunsparce.health <= 0:
            # you beat him!
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # add win text
            text_object.update_text('You lost the battle!', 30)
            text_object.update_position(175, 560)
            screen.blit(text_object.get_text_surface(),
                        (text_object.x, text_object.y))

            NextGameState = 'LOSE'

        if NextGameState == 'WHAT':
            time.sleep(2)
            # erase old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            text_object.update_text('What will ' + dunsparce.name + ' do?', 28)
            text_object.update_position(135, 563)
            screen.blit(text_object.get_text_surface(),
                        (text_object.x, text_object.y))

            NextGameState = 'IDLE'

        # waits a frame to attack
        if NextGameState == 'ENEMY WILL ATTACK':
            time.sleep(1)
            NextGameState = 'ENEMY ATTACKS'

        if NextGameState == 'ENEMY TURN':
            time.sleep(1)
            # erase old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            behavior_roll = random.randint(1, 1)

            if behavior_roll == 1:
                # print behavior roll
                text_object.update_text(Enemy.name + ' attacks!', 30)
                text_object.update_position(190, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

                NextGameState = 'ENEMY WILL ATTACK'

        if NextGameState == 'ENEMY ATTACKS':
            # erase old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            result = Attack.test_attack(Enemy.power, 4)

            # enemy attack
            if result[1] == 'MISS':
                # change main text
                text_object.update_text(Enemy.name + ' missed!', 30)
                text_object.update_position(210, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))
            if result[1] == 'CRIT':
                # changes main text
                text_object.update_text(
                    'Critical Hit! ' + str(result[0]) + ' Damage dealt', 27)
                text_object.update_position(70, 563)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

                # changes health text (character took damage)
                hp_group.draw(screen)
                dunsparce.health_update(result[0])
                character_hp_text.update_text(
                    str(dunsparce.health) + '/' + str(dunsparce.max_health) + ' HP', 24)
                screen.blit(enenmy_hp_text.get_text_surface(),
                            (enenmy_hp_text.x, enenmy_hp_text.y))

                # reprint character text too...
                screen.blit(character_hp_text.get_text_surface(),
                            (character_hp_text.x, character_hp_text.y))

            # same calculation but without critial hit
            if result[1] == 'HIT':
                text_object.update_text(
                    'Hit! ' + str(result[0]) + ' Damage dealt', 30)
                text_object.update_position(160, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

                # changes health text (enemy took damage)
                hp_group.draw(screen)
                dunsparce.health_update(result[0])
                character_hp_text.update_text(
                    str(dunsparce.health) + '/' + str(dunsparce.max_health) + ' HP', 24)
                screen.blit(character_hp_text.get_text_surface(),
                            (character_hp_text.x, character_hp_text.y))

                # reprint character text too...
                screen.blit(enenmy_hp_text.get_text_surface(),
                            (enenmy_hp_text.x, enenmy_hp_text.y))

            # return to waiting state
            NextGameState = 'WHAT'

        # if attack button is clicked
        if NextGameState == 'ATTACK':
            # erases old text by putting an 'eraser' white button on it
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # stores result as a list
            result = Attack.test_attack(dunsparce.power, 10)

            # result -> display result text and subtract health.
            if result[1] == 'MISS':
                text_object.update_text('You missed!', 30)
                text_object.update_position(290, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))
            if result[1] == 'CRIT':
                # changes main text
                text_object.update_text(
                    'Critical Hit! ' + str(result[0]) + ' Damage dealt', 27)
                text_object.update_position(70, 563)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

                # changes health text (enemy took damage)
                hp_group.draw(screen)
                Enemy.health_update(result[0])
                enenmy_hp_text.update_text(
                    str(Enemy.health) + '/' + str(Enemy.max_health) + ' HP', 24)
                screen.blit(enenmy_hp_text.get_text_surface(),
                            (enenmy_hp_text.x, enenmy_hp_text.y))

                # reprint character text too...
                screen.blit(character_hp_text.get_text_surface(),
                            (character_hp_text.x, character_hp_text.y))

            # same calculation but without critial hit
            if result[1] == 'HIT':
                text_object.update_text(
                    'Hit! ' + str(result[0]) + ' Damage dealt', 30)
                text_object.update_position(160, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

                # changes health text (enemy took damage)
                hp_group.draw(screen)
                Enemy.health_update(result[0])
                enenmy_hp_text.update_text(
                    str(Enemy.health) + '/' + str(Enemy.max_health) + ' HP', 24)
                screen.blit(enenmy_hp_text.get_text_surface(),
                            (enenmy_hp_text.x, enenmy_hp_text.y))

                # reprint character text too...
                screen.blit(character_hp_text.get_text_surface(),
                            (character_hp_text.x, character_hp_text.y))

            # return to waiting state
            NextGameState = 'ENEMY TURN'

        if NextGameState == 'FLEE':
            # erase old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)
            # attempt a flee
            result = Flee.try_flee()

            # update text and change 'flee' flag if necessary
            if result == 'FLEE':
                text_object.update_text(
                    str(dunsparce.name) + ' fled successfully!', 26)
                text_object.update_position(100, 560)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))
                Fleed = True

            if result == 'FAIL':
                text_object.update_text(
                    str(dunsparce.name) + ' tried to flee and failed!', 24)
                text_object.update_position(40, 563)
                screen.blit(text_object.get_text_surface(),
                            (text_object.x, text_object.y))

            # return to waiting state
            NextGameState = 'ENEMY TURN'

        if NextGameState == 'HEAL':
            # erase old text
            eraser_group.add(Eraser)
            eraser_group.update()
            eraser_group.draw(screen)

            # changes main text
            text_object.update_text(dunsparce.name + ' healed 10 health!', 28)
            text_object.update_position(90, 563)
            screen.blit(text_object.get_text_surface(),
                        (text_object.x, text_object.y))

            # changes health text (dunsparce healed)
            hp_group.draw(screen)
            dunsparce.heal()
            character_hp_text.update_text(
                str(dunsparce.health) + '/' + str(dunsparce.max_health) + ' HP', 24)
            screen.blit(enenmy_hp_text.get_text_surface(),
                        (enenmy_hp_text.x, enenmy_hp_text.y))

            # reprint character text too...
            screen.blit(character_hp_text.get_text_surface(),
                        (character_hp_text.x, character_hp_text.y))

            NextGameState = 'ENEMY TURN'

        # print(clock)
        # screen.fill(BLACK)
        active_characters.update()
        active_characters.draw(screen)
        active_buttons.update()
        active_buttons.draw(screen)
        pygame.display.flip()

# 002 - enemy dunsparce, 001 - character dunsparce


c_gen = random.randint(2, 4)
wild_spawn = ('00' + str(c_gen))
# battle_start('001', wild_spawn)


# battle_start('001', '003')image.png
