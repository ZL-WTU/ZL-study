class Settings():
    #存储所有设置的类
    def __init__(self):
        #初始化游戏的静态设置
        #屏幕设置
        self.screen_width=1600
        self.screen_height=1000
        self.bg_color=(230,230,230)

        #飞船的设置
        self.ship_speed_factor = 1.5          #但rect的centerx等属性只能存储整数
        self.ship_limit = 3                   #初始飞船数量

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60,60,60  #深灰色
        self.bullets_allowed=999999999

        #外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        #初始化游戏属性
        self.initialize_dynamic_settings()

        #计分
        self.alien_points = 50


    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed_factor =1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction为1表示向右，-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        #加速设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale




