import pyxel
import math
import trump
import fire
import mexico_status
import mexican_wall
import mexican_people
import transfer_bar


# 定数

SCREEN_WIDTH = 210
SCREEN_HEIGHT = 120

TRUMP_X = SCREEN_WIDTH / 3
TRUMP_Y = SCREEN_HEIGHT / 2
TRUMP_SPEED = 1

FIRE_SPEED = 2

WALL_POSITION = [35, 40, 45, 50]
PEOPLE_POSITION = [30, 40, 50, 60, 70, 80]
MP_NUM = 6


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load('assets/contents.pyxel')

        self.fires = []
        self.trump = trump.Trump(TRUMP_X, TRUMP_Y, TRUMP_SPEED)

        ## メキシコ
        self.mStatus = mexico_status.MexicoStatus()
        self.mWall = [mexican_wall.MexicanWall(x=n) for n in WALL_POSITION]
        self.mPeople = [mexican_people.MexicanPeople(0, n) for n in PEOPLE_POSITION]
        self.tBar = transfer_bar.TransferBar()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.input_shoot_fire(self.trump.x, self.trump.y, FIRE_SPEED)
        self.trump.update()
        self.fires_update()

        ## メキシコ
        self.mWall[self.mStatus.wall_position].update(damage=self.tBar.value)
        self.mStatus.update(w_health=self.mWall[self.mStatus.wall_position].health)
        for i in range(MP_NUM):
          self.mPeople[i].update(xIdx=self.mStatus.people_position)

        self.tBar.update()

    def draw(self):
        pyxel.cls(0)
        self.trump.draw()
        self.fires_draw()

        ## メキシコ
        for i in range(len(self.mWall)):
          self.mWall[i].draw()
        for i in range(MP_NUM):
          self.mPeople[i].draw()
        self.tBar.draw()


    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def input_shoot_fire(self, x, y, speed):
        if pyxel.btnp(pyxel.KEY_F):
            self.fires.append(fire.Fire(x, y, speed))

    def fires_update(self):
        for fire in self.fires:
            fire.update()

    def fires_draw(self):
        for fire in self.fires:
            fire.draw()


App()
