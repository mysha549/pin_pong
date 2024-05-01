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

speed_x = 3
speed_y = 3
player1 = Player('tubik_kleya.png', 50, 50, 8, 50, 75)
player2 = Player('tubik_kleya.png', 600, 50, 8, 50, 75)
ball = GameSprite('kubik_lego.png', 350, 250, 1, 50, 50)

font.init()
font1 = font.SysFont('Arial', 36)

font2 = font.SysFont('Arial', 55)
text_proigrish = font2.render('победил игрок 2', 1, (255, 0, 0))
text_proigrish2 = font2.render('победил игрок 1', 1, (0, 255, 0))

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
        if sprite.collide_rect(player1, ball):
            speed_x *= -1
        if sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(text_proigrish, (175, 250))
        if ball.rect.x > 700:
            finish = True
            window.blit(text_proigrish2, (175, 250))



    
    display.update()
    clock.tick(FPS)
