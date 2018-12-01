import pyxel


class TransferBar:

  def __init__(self):
    self.value = 50
  

  def update(self):

    ## 標準で減算
    self.value -= 1

    ## ボタンが押されたら加算
    if pyxel.btnp(pyxel.KEY_C):
      self.value += 1

    ## 数値の調整
    if self.value < 0:
      self.value = 0
    elif self.value > 100:
      self.value = 100
    
  
  def draw(self):

    ## バーを描画
    box_num = self.value // 5
    pyxel.rect(20, 180, 50*box_num, 190, 7)
