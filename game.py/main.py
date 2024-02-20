#ターミナル表示
#オブジェクト指向 

from game import Game
from character import Godzila,Kingkong   #ゴジラとキングコングをインポート


godzila = Godzila()       
kingkong = Kingkong() 
game = Game(godzila,kingkong)    
game.battle()

