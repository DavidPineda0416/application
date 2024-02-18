#ターミナルで遊べるポケモン
#オブジェクト指向 勉強

from game import Game
from pokemon import Pikachu,Hitokage   #ピカチュウとヒトカゲをインポート

game = Game()
pikachu = Pikachu()       #インスタンス化
hitokage = Hitokage()     #インスタンス化
game.battle(pikachu,hitokage)

