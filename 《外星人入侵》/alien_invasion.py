import pygame               #pygame包含开发游戏需要的功能
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group         #编组类似于列表，但提供了有助于开发游戏的额外功能
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建Play按钮
    play_button = Button(ai_settings,screen,'Play')

    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets=Group()

    #创建一个用于存储外星人的编组
    aliens=Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个用于存储游戏统计信息的实例,并创建得分牌
    stats=GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #开始游戏主循环
    while True:
        #监听鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens)

        if stats.game_active:
            # 控制飞船移动
            gf.fire_bullet(ai_settings,screen,ship,bullets)   #激光外挂
            ship.update()
            bullets.update()                        #当对编组调用update（）时，编组将自动对其中的每个精灵都调用update（）
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb)

run_game()