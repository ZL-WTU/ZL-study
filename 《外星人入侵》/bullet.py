import pygame
from pygame.sprite import Sprite        #将游戏中相关的元素编组，进而同时操作编组中的所有元素

class Bullet(Sprite):
    #对飞船发射的子弹进行管理的类

    def __init__(self,ai_settings,screen,ship):
        #在飞船所处的位置创建一个子弹对象
        super().__init__()
        self.screen=screen

        #在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height) #子弹并非基于图像，因此必须使用
        self.rect.centerx=ship.rect.centerx #pygame.Rect()类从空白开始创建一个矩形。需提供矩形左上角的X,Y坐标以及宽度和高度
        self.rect.top=ship.rect.top

        #存储用小数表示的子弹位置
        self.y=float(self.rect.y)       #定义了self.rect.centerx的初始值，self.rect.y的初始值会自动确定

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        #向上移动子弹
        #更新表示子弹的rect的小数值
        self.y-=self.speed_factor     #因为pygame中圆点在左上角，因此顶端y是0，向上移动即y--
        #更新表示子弹的rect的位置
        self.rect.y=self.y

    def draw_bullet(self):
        #在屏幕上绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)