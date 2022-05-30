import pygame
from baseitem import BaseItem
from explode import Explode


class Bullet(BaseItem):
    def __init__(self, main_game, name, speed, tank):
        # 加载子弹图片
        self.image = pygame.image.load("img/{}.png".format(name))
        self.direction = tank.direction
        self.speed = speed
        self.rect = self.image.get_rect()
        # 初始化子弹初始位置
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height/3*2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height/3*2
        # 记录子弹是否活着
        self.live = True
        self.main_game = main_game

    # 子弹移动方法
    def bullet_move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False  # 子弹消亡
        elif self.direction == 'D':
            if self.rect.top < self.main_game.screen_height - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live = False  # 子弹消亡
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False  # 子弹消亡
        elif self.direction == 'R':
            if self.rect.left < self.main_game.screen_width - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live = False  # 子弹消亡

    # 显示子弹方法
    def display_bullet(self, window):
        window.blit(self.image, self.rect)

    # 我方子弹碰撞敌方tank
    def hit_enemy_tank(self):
        for tank in self.main_game.enemy_tanks:
            if pygame.sprite.collide_rect(self, tank):
                # 产生爆炸效果
                explode = Explode(tank)
                self.main_game.explode_list.append(explode)
                self.live = False
                tank.live = False

    # 敌方子弹碰撞我方tank
    def hit_my_tank(self):
        for tank in self.main_game.players:
            if pygame.sprite.collide_rect(self, tank):
                # 产生爆炸效果
                explode = Explode(tank)
                self.main_game.explode_list.append(explode)
                self.live = False
                tank.live = False

    # 子弹碰撞墙壁
    def hit_walls(self):
        pass
