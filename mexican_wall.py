"""
メキシコの壁
"""
import pyxel


class MexicanWall:

  def __init__(self, x, y=20):

    ## 壁の位置
    self.x = x
    self.y = y

    ## 壁の状態
    self.health = 100
    self.visible = True


  def update(self, damage):

    ## 壁の体力
    if damage < 0:
      self.health += damage

    ## 表示の有無
    if self.health <= 0:
      self.visible = False


  def draw(self):

    ## VisibleがTrueなら表示
    if self.visible:
      pyxel.blt(self.x, self.y, 1, 0, 0, 2, 80)
