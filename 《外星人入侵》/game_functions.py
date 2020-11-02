import sys                    #sys模块用于退出游戏
import pygame
from bullet import Bullet

def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_enents(event,ai_settings,screen,ship,bullets):
    #响应按下
    if event.key == pygame.K_RIGHT:                                     #注意.key才是针对具体按键
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
         fire_bullet(ai_settings,screen,ship,bullets)


def check_events(ai_settings,screen,ship,bullets):
    #响应鼠标和按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:                    #KEYDOWN事件是键盘按下动作发生时产生的消息
            check_keydown_enents(event,ai_settings,screen,ship,bullets)

        elif event.type==pygame.KEYUP:                      #KEYUP事件是键盘松开动作发生时产生的消息
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    #更新屏幕上的图像，并切换到新屏幕
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():                      #方法bullets。sprites（）返回一个列表，其中包含编组bullets中的所有精灵
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    # 删除已经消失的子弹
    for bullet in bullets.copy():  # 不应从列表或编组中删除条目，因此必须遍历编组的副本，方法copy（）会复制一个副本
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
        #检查子弹数量
        if len(bullets)< ai_settings.bullets_allowed:
            #创建一颗子弹，并将其加入到编组bullets中
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

