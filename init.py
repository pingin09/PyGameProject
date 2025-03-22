import pygame as pg
import sys
import math

from pygame.draw import circle

pg.init()
print("call of war\nWW3\n\n\n\n")
screen = pg.display.set_mode((800,800))
pg.display.set_caption("Call of war, world war three")
map_image = pg.image.load("Map_image.jpg")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

player = [
    {"name": "Stalin",
     "color": (180, 0, 0),
     "arms to place": 2},
    {"name": "Trump",
     "color": (180, 0, 0),
     "arms to place": 2},
]

country = [
    {"x":530,
     "y": 230,
     "name": "USSR",
     "arms": 0,
     "slawes": 159,
     "people": 30987669,
     "people+": 480000,
     "owner": None},
    {"x": 158,
     "y": 242,
     "name": "USA",
     "arms": 0,
     "slawes": 159,
     "people": 30987669,
     "people+": 480000,
     "owner": None}
]

current_player_index = 0

pg.font.init()
font = pg.font.SysFont(None, 24)
running = True
map_image = pg.transform.scale(map_image,(800,800))
selected_territory = None


while running:
    screen.blit(map_image, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"x {x}, y {y}")
            for country1 in country:
                dist = math.hypot(x - country1['x'], y - country1['y'])
                if dist < 10:
                    selected_territory = country1
                    print(f"Вы выбрали текущую территорию, {country1["name"]}")
                    current_player = player[current_player_index]
                    if current_player["arms to place"] > 0:
                        if (country["owner"] is None) or (country["owner"] == current_player_index):
                            if country["owner"] is None:
                                country["owner"] = current_player_index
                            country["arms"] += 1
                            current_player["arms to place"] -= 1
                            print(f"{current_player["name"]} разместил армию на {country["name"]}. Осталось армий: {current_player["arms to place"]}")
                            if current_player["arms to place"]:
                                current_player_index = (current_player_index+1) % len(player)
                                print(f'Теперь ход у {player[current_player_index["name"]]}')


    for country1 in country:
        arms = country1['arms']
        x = country1["x"]
        y = country1['y']
        if country1 == selected_territory:
            circle_color = green
        else:
            circle_color = red
        pg.draw.circle(screen, circle_color, (country1["x"], country1["y"]), 10)
        text_arm = font.render(f'Армий {str(arms)}',True, red)
        text_rect = text_arm.get_rect(center=(x, y + 20))
        screen.blit(text_arm, text_rect)

    pg.display.flip()
