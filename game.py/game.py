#ゲームの管理


class Game:
  def __init__(self, monster1,monster2):
    self._monster1 = monster1
    self._monster2 = monster2
  
  def battle(self):
      self._start()
      winner, loser = self._attack()
      self._show_result(winner, loser)
      return
      
      self._monster1.attack(self._monster2)
      self._monster2.attack(self._monster1)
    
  def _start(self):
    print(f'{self._monster1.name}が現れた。{self._monster1.name}のHPは{self._monster1.hp}だ。')
    print(f'{self._monster2.name}が現れた。{self._monster2.name}のHPは{self._monster2.hp}だ。')
  
  def _attack(self):
    while True:
      self._monster1.attack(self._monster2)
      if self._monster2.is_fainted():
        return(self._monster1, self._monster2)
  
      self._monster2.attack(self._monster1)
      if self._monster1.is_fainted():
        return(self._monster2, self._monster1)
  
  
  def _show_result(self, winner, loser):
    print(f'{loser.name}は倒れた。{winner.name}の勝ち！')
    