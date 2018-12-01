import pyxel


class Fire:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.x += self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 8)
