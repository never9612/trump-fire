import pyxel
import trump
import fire


# 定数

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

TRUMP_X = SCREEN_WIDTH / 2
TRUMP_Y = SCREEN_HEIGHT / 2
TRUMP_SPEED = 1

FIRE_SPEED = 2


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.fires = []
        self.trump = trump.Trump(TRUMP_X, TRUMP_Y, TRUMP_SPEED)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.input_shoot_fire(self.trump.x, self.trump.y, FIRE_SPEED)
        self.trump.update()
        self.fires_update()

    def draw(self):
        pyxel.cls(0)
        self.trump.draw()
        self.fires_draw()

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
