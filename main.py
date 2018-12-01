import pyxel
import math
import random
import trump
import fire
import flower
import enemy


# 定数

SCREEN_WIDTH = 210
SCREEN_HEIGHT = 120

TRUMP_X = SCREEN_WIDTH / 3
TRUMP_Y = SCREEN_HEIGHT / 2
TRUMP_SPEED = 1

FIRE_SPEED = 2

FLOWERS_ROW = 13
FLOWERS_COL = 6
FLOWER_SIZE = 8

FIELD_X = 160
FIELD_Y = 8
FIELD_WIDTH = FLOWER_SIZE * FLOWERS_COL - FLOWER_SIZE
FIELD_HEIGHT = FLOWER_SIZE * FLOWERS_ROW - FLOWER_SIZE

OBAMA_X = FIELD_X
OBAMA_Y = FIELD_Y
OBAMA_MOVE_INTERVAL = 10

HILLARY_X = FIELD_X
HILLARY_Y = FIELD_X
HILLARY_MOVE_INTERVAL = 10


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load('assets/contents.pyxel')

        self.fires = []
        self.flowers = []
        self.trump = trump.Trump(TRUMP_X, TRUMP_Y, TRUMP_SPEED)
        self.obama = enemy.Obama(
            OBAMA_X, OBAMA_Y, OBAMA_MOVE_INTERVAL, FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT)
        self.hillary = enemy.Hillary(
            HILLARY_X, HILLARY_Y, HILLARY_MOVE_INTERVAL, FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        self.shoot_fire(self.trump.x, self.trump.y, FIRE_SPEED)
        self.check_fire_hit_flower()
        self.plant_flower(self.obama.x, self.obama.y)
        self.trump.update()
        self.obama.update()
        self.hillary.update()
        self.flowers_update()
        self.fires_update()

    def draw(self):
        pyxel.cls(0)
        self.trump.draw()
        self.fires_draw()
        self.flowers_draw()
        self.obama.draw()
        self.hillary.draw()

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def shoot_fire(self, x, y, speed):
        if pyxel.btnp(pyxel.KEY_F):
            self.fires.append(fire.Fire(x, y, speed))

    def fires_update(self):
        for i, fire in enumerate(self.fires):
            fire.update()
            if not fire.is_alive:
                del self.fires[i]

    def fires_draw(self):
        for fire in self.fires:
            fire.draw()

    def plant_flower(self, x, y):
        self.flowers.append(flower.Flower(x, y))
        self.flowers.append(flower.Flower(x + 8, y))
        self.flowers.append(flower.Flower(x, y + 8))
        self.flowers.append(flower.Flower(x + 8, y + 8))
        self.flowers = list(set(self.flowers))

    def check_fire_hit_flower(self):
        for fire in self.fires:
            for flower in self.flowers:
                if self.distance(fire.x, fire.y, flower.x, flower.y) < FLOWER_SIZE and flower.is_burned == False:
                    fire.is_alive = False
                    flower.is_burned = True

    def flowers_update(self):
        for i, flower in enumerate(self.flowers):
            flower.update()
            if flower.burned_time >= 30:
                del self.flowers[i]

    def flowers_draw(self):
        for flower in self.flowers:
            flower.draw()

    def draw_field(self, x, y, w, h):
        pyxel.rectb(x, y, x+w, y+h, 7)


App()
