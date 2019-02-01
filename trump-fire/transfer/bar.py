import pyxel


class TransferBar:

  def __init__(self):

    ## バーの量
    self.value = 0
  
  def reset(self):
    """
    貿易収支のステータスを外部からリセットするときに使用
    """
    self.value = 0
  
  def update(self):

    ## 標準で減算
    self.value -= 0.5

    ## ボタンが押されたら加算
    if pyxel.btnp(pyxel.KEY_D):
      self.value += 7

    ## 数値の調整
    if self.value < -25:
      self.value = -25
    elif self.value > 25:
      self.value = 25
    
  def draw(self):

    # バーの色: 正なら赤、負なら青
    barColor = 8 if self.value >= 0 else 12

    # バーを描画
    pyxel.rect(35, 110, self.value+35, 115, barColor)
