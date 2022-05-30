import pygame
from bullet import Bullet
from baseitem import BaseItem


class Tank(BaseItem):
    def __init__(self, main_game, name, speed, left, top):
        self.main_game = main_game
        self.images = {
            "U": pygame.image.load("img/{}_U.png".format(name)),
            "D": pygame.image.load("img/{}_D.png".format(name)),
            "L": pygame.image.load("img/{}_L.png".format(name)),
            "R": pygame.image.load("img/{}_R.png".format(name))
        }
        self.direction = "U"
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.bullet_list = []
        self.live = True

    # 坦克移动方法
    def move(self):
        if self.direction == "L" and not self.stop:
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R' and not self.stop:
            if self.rect.left + self.rect.width + 4 < self.main_game.screen_width:
                self.rect.left += self.speed
        elif self.direction == 'U' and not self.stop:
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D' and not self.stop:
            if self.rect.top + self.rect.height < self.main_game.screen_height:
                self.rect.top += self.speed

    # 碰撞墙壁方法
    def hit_walls(self):
        pass

    # 射击方法
    def shot(self, name, speed):
        # 产生一颗子弹
        m = Bullet(self.main_game, name, speed, self)
        self.bullet_list.append(m)

    # 显示tank方法
    def display_tank(self, window):
        self.image = self.images[self.direction]
        window.blit(self.image, self.rect)
