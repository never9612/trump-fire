import pyxel


class BossFlower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.growth_time = growth_time
        self.can_grow = False

    def update(self):
        if self.can_grow:
            self.growth_time += 1

    def draw(self):
        if self.is_burned and pyxel.frame_count % 4 < 2:
            pyxel.blt(self.x, self.y, 0, 0, 64, 8, 8, 0)
        elif self.is_burned and pyxel.frame_count % 4 >= 2:
            pyxel.blt(self.x, self.y, 0, 8, 64, 8, 8, 0)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 32, 8, 8, 0)
