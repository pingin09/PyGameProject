import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((800,800))
pg.display.set_caption("Call of war, world war three")
map_image = pg.image.load("Map_image.jpg")

running = True
map_image = pg.transform.scale(map_image,(800,800))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(map_image,(0,0))
    pg.draw.circle(screen, (180, 0, 0), (650, 350), 2)
    pg.display.flip()
