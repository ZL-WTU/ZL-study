import sys                  #sys模块用于退出游戏
import pygame               #pygame包含开发游戏需要的功能
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #创建一艘飞船
    ship=Ship(screen)

    #开始游戏主循环
    while True:
        #监听鼠标和键盘事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #每次循环都重绘屏幕
        screen.fill(ai_setting.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()