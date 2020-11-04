import pygame

class Ship():

    def __init__(self,ai_settings,screen):

        # 初始化飞船并设置初始位置
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()                 #飞船矩形
        self.screen_rect=screen.get_rect()              #屏幕矩形

        #将每艘新飞船放在底部中央
        self.rect.centerx=self.screen_rect.centerx     #centerx表示飞船中心的x坐标
        self.rect.bottom=self.screen_rect.bottom       #bottom表示飞船下边缘的y坐标

        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)

        #飞船移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #根据移动标志调整飞船位置
        #更新飞船的center值，而非rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:                           #pygame中左上角为坐标轴圆点，因此左边缘x坐标为0
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)                              #blit()方法是位块传送，即传送图片
                                                                            #draw（）是绘制基本图形
                                                                            #fill()是填充颜色
    def center_ship(self):
        #将飞船在屏幕上居中
        self.center = self.screen_rect.centerx