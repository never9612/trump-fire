import pyxel


class MexicoPeople:

  # 定数
  PARAM_MOVE = 15

  def __init__(self, xIdx, y, attack=False):

    # ポジション
    self.position_x = [25, 30, 35, 40]
    
    # 攻撃
    self.param_attack = 0
    self.attack       = attack

    self.x = self.position_x[xIdx]
    self.y = y
  
  def update(self, xIdx):
    self.x = self.position_x[xIdx]

    # 進退を入れ替え
    self.param_attack += 1
    if self.param_attack > self.PARAM_MOVE:
      self.attack       = not self.attack
      self.param_attack = 0

    # 攻撃姿勢なら前進; そうでなければ後退
    if self.attack:
      self.x += 2
    else:
      self.x -= 2
  
  def draw(self):
    pyxel.blt(self.x, self.y, 0, 1, 16, 7, 8)
