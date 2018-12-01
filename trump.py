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
        elif self.y >= pyxel.height:
            self.y = pyxel.height

    def draw(self):
        pyxel.circ(self.x, self.y, 4, 7)
