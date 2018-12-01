import pyxel


class Fire:
    def __init__(self, x, y, speed):
        self.x = x + 6
        self.y = y + 7
        self.speed = speed
        self.is_alive = True

    def update(self):
        self.x += self.speed

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 56, 4, 4, 0)
