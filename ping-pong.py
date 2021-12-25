from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption("Пинг-Понг")
FPS = 60
clock = time.Clock()
back = (200, 255, 255)
window.fill(back)
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)