import pyxel
import random


class Enemy:
    def __init__(self, x, y, move_interval, ax, ay, aw, ah):
        self.x = x
        self.y = y
        self.move_interval = move_interval
        self.ax = ax
        self.ay = ay
        self.aw = aw
        self.ah = ah

    def update(self):
        if pyxel.frame_count % self.move_interval == 0:
            self.x = random.randrange(self.ax, self.ax + self.aw, 8)
            self.y = random.randrange(self.ay, self.ay + self.ah, 8)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)


class Obama(Enemy):
    def __init__(self, x, y, move_interval, ax, ay, aw, ah):
        super().__init__(x, y, move_interval, ax, ay, aw, ah)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 0)


class Hillary(Enemy):
    def __init__(self, x, y, move_interval, ax, ay, aw, ah):
        super().__init__(x, y, move_interval, ax, ay, aw, ah)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, 0)
