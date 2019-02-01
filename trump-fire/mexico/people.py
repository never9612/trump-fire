import pyxel


class MexicoPeople:

  def __init__(self, xIdx, y):

    self.position = [25, 30, 35, 40]

    self.x = self.position[xIdx]
    self.y = y
  
  def update(self, xIdx):
    self.x = self.position[xIdx]
  
  def draw(self):
    pyxel.blt(self.x, self.y, 0, 1, 16, 7, 8)
