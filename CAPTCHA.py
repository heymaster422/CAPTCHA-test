import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('test-tube-start.png'))
        self.sprites.append(pygame.image.load('test-tube-1.png'))
        self.sprites.append(pygame.image.load('test-tube-1.5.png'))
        self.sprites.append(pygame.image.load('test-tube-2.png'))
        self.sprites.append(pygame.image.load('test-tube-2.5.png'))
        self.sprites.append(pygame.image.load('test-tube-3.png'))
        self.sprites.append(pygame.image.load('test-tube-3.5.png'))
        self.sprites.append(pygame.image.load('test-tube-4.png'))
        self.sprites.append(pygame.image.load('test-tube-4.5.png'))
        self.sprites.append(pygame.image.load('test-tube-5.png'))
        self.sprites.append(pygame.image.load('test-tube-5.5.png'))
        self.sprites.append(pygame.image.load('test-tube-6.png'))
        self.sprites.append(pygame.image.load('test-tube-6.5.png'))
        self.sprites.append(pygame.image.load('test-tube-7.png'))
        self.sprites.append(pygame.image.load('test-tube-7.5.png'))
        self.sprites.append(pygame.image.load('test-tube-8.png'))
        self.sprites.append(pygame.image.load('test-tube-8.5.png'))
        self.sprites.append(pygame.image.load('test-tube-max.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]


#starts the animation
    def start(self):
        self.attack_animation = True

        
#Keeps the animation going until it reaches the end. 
    def update(self,speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]
    def stop(self):
        self.attack_animation = False
# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CAPTCHA TEST")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(250,300)
moving_sprites.add(player)
#Keeps the game running. 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.start()
        if event.type == pygame.KEYDOWN:
            player.stop()

    # Drawing
    screen.fill((250,250,250))
    moving_sprites.draw(screen)
    moving_sprites.update(0.50)
    pygame.display.flip()
    clock.tick(60)