import pyxel


class MexicoStatus:

  def __init__(self):

    # ステータス
    self.status     = True  #ゲームの状態
    self.wall_num   = 4     #壁の枚数
    self.people_num = 6     #メキシコ人の数

    # 初期位置
    self.wall_position   = 0
    self.people_position = 0
  

  def update(self, w_health):

    # 壁が壊れたとき
    if w_health <= 0:
      self.wall_position   += 1
      self.people_position += 1
    
    # 壁が全て破壊されたらゲーム終了
    if self.wall_position == self.wall_num-1:
      self.status = False


  def draw(self):

    # 描画物なし
    pass
