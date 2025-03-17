from itertools import count

import pygame as pg
import sys
pg.init()
print("call of war\nWW3\n\n\n\n")
screen = pg.display.set_mode((800,800))
pg.display.set_caption("Call of war, world war three")
map_image = pg.image.load("Map_image.jpg")

country = [
    {"x":530,
     "y": 230,
     "name": "USSR",
     "arms": 99999,
     "slawes": 159,
     "people": 30987669,
     "people+": 480000},
    {"x": 158,
     "y": 242,
     "name": "USA",
     "arms": 99999,
     "slawes": 159,
     "people": 30987669,
     "people+": 480000}
]

pg.font.init()
font = pg.font.SysFont(None, 24)

running = True
map_image = pg.transform.scale(map_image,(800,800))
while running:
    screen.blit(map_image, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"x {x}, y {y}")
    for country1 in country:
        pg.draw.circle(screen, (255, 255, 255), (country1["x"], country1["y"]), 5)
    pg.display.flip()
