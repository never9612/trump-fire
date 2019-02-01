import pyxel
import math
import random
from trump import trump, fire
from enemy import enemy, flower, boss_flower
from mexico.status import MexicoStatus
from mexico.people import MexicoPeople
from mexico.wall import MexicoWall
from transfer.bar import TransferBar


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
OBAMA_MOVE_INTERVAL = 100

HILLARY_X = FIELD_X
HILLARY_Y = FIELD_X
HILLARY_MOVE_INTERVAL = 100

WALL_POSITION = [35, 40, 45, 50]
PEOPLE_POSITION = [30, 40, 50, 60, 70, 80]
MP_NUM = 6


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load('assets/contents.pyxel')

        # 民主党の花
        self.fires = []
        self.flowers = []
        self.trump = trump.Trump(TRUMP_X, TRUMP_Y, TRUMP_SPEED)
        self.obama = enemy.Obama(
            OBAMA_X, OBAMA_Y, OBAMA_MOVE_INTERVAL, FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT)
        self.hillary = enemy.Hillary(
            HILLARY_X, HILLARY_Y, HILLARY_MOVE_INTERVAL, FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT
        )

        # メキシコ
        self.mStatus = MexicoStatus()
        self.mWall = [MexicoWall(x=n) for n in WALL_POSITION]
        self.mPeople = [MexicoPeople(0, n, attack=False if i % 2 == 0 else True) for i, n in enumerate(PEOPLE_POSITION)]

        # 貿易摩擦
        self.tBar = TransferBar()

        pyxel.run(self.update, self.draw)

    def update(self):
        # 火の発射
        self.shoot_fire(self.trump.x, self.trump.y, FIRE_SPEED)
        # 火と花の当たり判定
        self.check_fire_hit_flower()
        # 花を植える
        self.plant_flower(self.obama.x, self.obama.y)
        self.plant_flower(self.hillary.x, self.hillary.y)
        # トランプ更新
        self.trump.update()
        # オバマ・ヒラリー更新
        self.obama.update()
        self.hillary.update()
        # 花更新
        self.flowers_update()
        # 火更新
        self.fires_update()

        # メキシコ
        self.mWall[self.mStatus.wall_position].update(damage=self.tBar.value)
        self.mStatus.update(
            w_health=self.mWall[self.mStatus.wall_position].health)
        for i in range(MP_NUM):
            self.mPeople[i].update(xIdx=self.mStatus.people_position)

        self.tBar.update()

    def draw(self):
        pyxel.cls(0)
        # トランプ・火・花・オバマ・ヒラリー
        self.trump.draw()
        self.fires_draw()
        self.flowers_draw()
        self.obama.draw()
        self.hillary.draw()

        # メキシコ
        for i in range(len(self.mWall)):
            self.mWall[i].draw()
        for i in range(MP_NUM):
            self.mPeople[i].draw()
        self.tBar.draw()

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
