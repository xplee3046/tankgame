import pygame


class Explode:
    def __init__(self, tank):
        self.rect = tank.rect
        self.step = 0
        self.images = [pygame.image.load("img/explode/{}.png".format(i)) for i in range(1, 17)]
        self.image = self.images[self.step]
        self.live = True

    # 显示爆炸方法
    def display_explode(self, window):
        if self.step < len(self.images):
            self.image = self.images[self.step]
            window.blit(self.image, self.rect)
            self.step += 1
        else:
            self.live = False
            self.step = 0
