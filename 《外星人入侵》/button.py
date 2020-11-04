import pygame.font      #pygame.font用于将文本渲染到屏幕上

class Button():

    def __init__(self,ai_settings,screen,msg):
        #初始化按钮的属性
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #设置按钮的尺寸以及其他属性
        self.width,self.height = 200,50
        self.button_color = (255,255,0)
        self.text_color = (255,0,255)
        self.font = pygame.font.SysFont(None,48)   #pygame.font.SysFont()方法用于设置字体，实参None表示默认字体，48则是字号

        #创建按钮的rect对象，并使其剧中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        #将msg渲染为图像，并使其在按钮上居中
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color) #font.render()方法将文本转换为图像
        self.msg_image_rect=self.msg_image.get_rect()                                  #第二个实参的布尔值指定是否开启抗锯齿
        self.msg_image_rect.center=self.rect.center                                     #第三个指定文本颜色，第四个指定背景色

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
