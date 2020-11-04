import sys                    #sys模块用于退出游戏
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep       #sleep函数可以让游戏暂停

def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #响应按下
    if event.key == pygame.K_RIGHT:                                     #注意.key才是针对具体按键
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #pygame.key.set_repeat(10,10)    #每一毫秒发送一个KEYDOWN事件，发送间隔一毫秒（小外挂）
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens):
    #响应鼠标和按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:                    #KEYDOWN事件是键盘按下动作发生时产生的消息
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type==pygame.KEYUP:                      #KEYUP事件是键盘松开动作发生时产生的消息
            check_keyup_events(event,ship)

        elif event.type==pygame.MOUSEBUTTONDOWN:              #MOUSEBUTTONDOWN事件是鼠标按下动作发生时产生的消息
            mouse_x,mouse_y = pygame.mouse.get_pos()          #pygame.mouse.get_pos()返回一个元祖，包含玩家单击鼠标的x,y坐标
            check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets)

def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets):
    #在玩家单击Play按钮时开始新游戏
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y) #rect.collidepoint()检查鼠标单击位置是否在Play按钮的rect内
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)     #向set_visible（）传递False，让Pygame在光标位于窗口内时将其隐藏起来

        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb):
    #更新屏幕上的图像，并切换到新屏幕
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():                      #方法bullets。sprites（）返回一个列表，其中包含编组bullets中的所有精灵
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #显示得分
    sb.show_score()

    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb):
    # 删除已经消失的子弹
    for bullet in bullets.copy():  # 不应从列表或编组中删除条目，因此必须遍历编组的副本，方法copy（）会复制一个副本
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True , True)   #pygame.sprite.groupcollide两个精灵组碰撞检测、

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points *len(aliens)
            sb.prep_score()

    if len(aliens) == 0:         #即外星人已经被消灭干净
        # 删除现有的子弹,加快游戏节奏，并新建一群外星人
        bullets.empty()  # 调用empty（）方法删除现有的所有子弹
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
        #检查子弹数量
        if len(bullets)< ai_settings.bullets_allowed:
            #创建一颗子弹，并将其加入到编组bullets中
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    #计算每行容纳多少个外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 计算可容纳外星人的水平空间，两边都预留一个外星人的宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 计算水平空间可容纳外星人的个数，并用int取整
    return  number_aliens_x

def get_number_rows(ai_setting,ship_height,alien_height):
    #计算可容纳多少行外星人
    available_space_y=(ai_setting.screen_height-3*(alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个外星人并将其放在当前行
    # 外星人的间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width                          # 将rect属性中的宽度赋给alienw_width避免rect被反复访问
    alien.x = alien_width + 2 * alien_width * alien_number  # 外星人的X坐标
    alien.rect.x = alien.x                                  # 确定外星人图像的X坐标
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number           #确定外星人图像的Y坐标
    aliens.add(alien)                                   # add（element）,将element当做一个整体插入字典中，若已存在则不任何执行操作

def create_fleet(ai_settings,screen,ship,aliens):
    #创建外星人群
    #创建一个外星人，并计算一行可以容纳多少外星人
    alien=Alien(ai_settings,screen)
    number_aliens_x=(get_number_aliens_x(ai_settings,alien.rect.width))
    #确定行数
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)-3

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    #有外星人到达边缘时采取相应措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    #将整群外星人下移，并改变方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    #响应被外星人撞到的飞船

    if stats.ships_left > 1:
        #将ship_left减1
        stats.ships_left -= 1

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  #游戏结束后显示光标

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    #检查是否有外星人到达屏幕底端
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #与飞船被撞到一样的处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    #检查外星人是否位域屏幕边缘，并更新外星人群中所有外星人的位置
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):            #方法spritecollideany（）接受两个实参，一个精灵和一个编组它检查编组
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets) #是否有成员与精灵发生了碰撞,找到与精灵发生碰撞的编组成员后
    #检查是否有外星人到达屏幕底端                                   #就停止遍历编组,如果没有发生碰撞，则返回None
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)