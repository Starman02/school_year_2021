import pygame
import random
import math

pygame.font.init()
pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((900, 720))
pygame.display.set_caption("Sprite test")
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
        return damage, status_update


def battle_start():
    # tracks the current game operation
    NextGameState = 'IDLE'

    # spawns button objects
    Attack = Button(BLUE, 280, 100, 'Attack Button')
    Items = Button(RED, 280, 100, 'Items Button')
    Flee = Button(GREEN, 280, 100, 'Flee Button')

    # Attack position
    Attack.rect.x = 10
    Attack.rect.y = 600

    # Items Position
    Items.rect.x = 306
    Items.rect.y = 600

    # Flee Position
    Flee.rect.x = 600
    Flee.rect.y = 600

    # creates and adds buttons to group
    active_buttons = pygame.sprite.Group()
    active_buttons.add(Attack)
    active_buttons.add(Items)
    active_buttons.add(Flee)

    running = True
    while running:
        clock.tick(60)
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

        if NextGameState == 'ATTACK':
            print(Attack.test_attack(50, 10))
            NextGameState = 'IDLE'

        # print(clock)
        # screen.fill(BLACK)
        active_buttons.update()
        active_buttons.draw(screen)
        pygame.display.flip()


battle_start()
