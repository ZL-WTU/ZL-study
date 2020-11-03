import pygame
from pygame.sprite import Sprite    #sprite英文释义是精灵，即在屏幕上显示的一个个角色，你要创建一个在屏幕上显示的角色
                                    # 就可以用pygame提供的sprite类中的很多有用的方法
class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #加载外星人图像并设置属性
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #设置外星人的位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #存储准确位置
        self.x=float(self.rect.x)

    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        #若外星人处于屏幕边缘就返回True
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #向左或右移动外星人
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction) #fleet_direction为正则+，向右
        self.rect.x=self.x                                                               #fleet_direction为负则-，向左


