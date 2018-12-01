import pyxel


class MexicanWall:

  def __init__(self, x, y=20):
    self.x = x
    self.y = y
    self.health = 50
    self.visible = True

  def update(self, score):

    ## 壁の体力
    if self.health + score > 100:
      self.health = 100
    elif self.health - score < 0:
      self.health = 0
    else:
      self.health += score

    ## 表示の有無
    if self.health <= 0:
      self.visible = False
  
  def draw(self):

    ## VisibleがTrueなら表示
    if self.visible:
      pyxel.blt(self.x, self.y, 1, 0, 0, 2, 80)
