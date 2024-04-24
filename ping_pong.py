from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('phon_mine.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

speed_x = 5
speed_y = 5
player1 = Player('tubik_kleya.png', 50, 50, 8, 50, 75)
player2 = Player('tubik_kleya.png', 650, 50, 8, 50, 75)
ball = GameSprite('kubik_lego.png', 350, 250, 0, 50, 50)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if finish != True:
        window.blit(background, (0, 0))
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

    
    display.update()
    clock.tick(FPS)
