import pygame
test = 0

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sprite test")
clock = pygame.time.Clock()

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


# spawns button objects
Attack = Button(BLUE, 200, 100, 'Attack Button')
Items = Button(RED, 200, 100, 'Items Button')
Flee = Button(GREEN, 200, 100, 'Flee Button')

# Attack position
Attack.rect.x = 10
Attack.rect.y = 350

# Items Position
Items.rect.x = 220
Items.rect.y = 350

# Flee Position
Flee.rect.x = 430
Flee.rect.y = 350

# creates and adds buttons to group
active_buttons = pygame.sprite.Group()
active_buttons.add(Attack)
active_buttons.add(Items)
active_buttons.add(Flee)

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Attack.check_clicked() == True:
                    print('Attack!')
                if Items.check_clicked() == True:
                    print('Items!')
                if Flee.check_clicked() == True:
                    print('Flee!')
                
        
        # screen.fill(BLACK)
        active_buttons.update()
        active_buttons.draw(screen)
        pygame.display.flip()


main()