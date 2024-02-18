#ポケモンの管理

class Pokemon:
    name = 'ピカチュウ'
    hp = 20
    atk = 10
    
    def __init__(self, name, hp, atk):    #初期化
      self.name = name
      self.hp = hp
      self.atk = atk
    
    
    def attack(self):
        print(f'{self.name}の攻撃！', end='')     # end='' 改行
        self.attack_message()
        
    def attack_message(self):
      pass
    
    
    
    
class Pikachu(Pokemon):    
  def __init__(self):
    super().__init__('ピカチュウ',20 ,10)   #親から継承 super().__init__   オーバライド
      
  def attack_message(self):
        print('10万ボルト！')
        
        
class Hitokage(Pokemon):
   def __init__(self):
     super().__init__('ヒトカゲ',18 ,5)
        
   def attack_message(self):
        print('ひのこ！')
             
        
        
         
              
        

