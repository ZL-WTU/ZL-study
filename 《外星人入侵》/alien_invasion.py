import pygame               #pygame包含开发游戏需要的功能
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    #开始游戏主循环
    while True:
        #监听鼠标和键盘事件
        gf.check_events(ship)

        # 控制飞船移动
        ship.update()

        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings,screen,ship)



run_game()