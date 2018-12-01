import pyxel


class Trump:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed

        if self.y <= 0:
            self.y = 0
        elif self.y >= pyxel.height - 16:
            self.y = pyxel.height - 16

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
