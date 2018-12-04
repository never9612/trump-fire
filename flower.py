import pyxel


class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_burned = False
        self.burned_time = 0

    def __eq__(self, other):
        if not isinstance(other, Flower):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(None)

    def update(self):
        if self.is_burned:
            self.burned_time += 1

    def draw(self):
        if self.is_burned and pyxel.frame_count % 4 < 2:
            pyxel.blt(self.x, self.y, 0, 0, 64, 8, 8, 0)
        elif self.is_burned and pyxel.frame_count % 4 >= 2:
            pyxel.blt(self.x, self.y, 0, 8, 64, 8, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 32, 8, 8, 0)
