from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('phon_mine.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    
    display.update()
    clock.tick(FPS)
