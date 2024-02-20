#モンスターの管理

class Monster:
    name = 'ゴジラ'
    hp = 200
    atk = 100
    
    def __init__(self, name, hp, atk):    #初期化
      self.name = name
      self.hp = hp
      self.atk = atk
    
    
    def attack(self, target):
        target.hp -= self.atk
        print(f'{self.name}の攻撃！', end='')     # end='' 改行
        self.attack_message(target)
        
    def attack_message(self, target):
      pass
    
    def is_fainted(self):
      return self.hp <= 0
      
    
    
class Godzila(Monster):    
  def __init__(self):
    super().__init__('ゴジラ',200 ,100)   #親から継承 super().__init__   オーバライド
      
  def attack_message(self, target):
        print(f'レーザービーム! {target.name}は{self.atk}ダメージをもらった！{target.name}のHPは{target.hp}だ！')
        
        
class Kingkong(Monster):
   def __init__(self):
     super().__init__('キングコング',200 ,80)
        
   def attack_message(self, target):
        print(f'パンチ！{target.name}は{self.atk}ダメージをもらった！{target.name}のHPは{target.hp}だ！')
             
        
        
         
              
        

