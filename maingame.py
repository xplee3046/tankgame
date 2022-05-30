import random

import pygame
import time
from mytank import MyTank
from enemytank import EnemyTank


class MainGame:
    COLOR_BLACK = pygame.Color(0, 0, 0)
    COLOR_RED = pygame.Color(255, 255, 255)
    window = None

    mytank_count = 1  # 玩家数量
    etank_count = 9  # 敌方tank数量

    player_speed = 1.5  # 玩家tank速度，必须>=1

    def __init__(self):
        self.screen_height = 600
        self.screen_width = 1000
        self.players = []
        self.enemy_tanks = []
        self.explode_list = []

    # 开始游戏
    def start_game(self):
        pygame.display.init()
        # 创建窗口
        MainGame.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        # 设置title
        pygame.display.set_caption("坦克大战 V1.1")

        # 创建我方坦克
        self.create_mytanks(MainGame.mytank_count)
        # 创建敌方坦克
        self.create_enemytank(MainGame.etank_count)

        # 窗口持续刷新
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            # 窗口添加文字说明
            MainGame.window.blit(self.get_text_surface("剩余敌方坦克: %d辆" % len(self.enemy_tanks)), (5, 5))

            # 显示我方tank
            for tank in self.players:
                if tank.live:
                    tank.display_tank(MainGame.window)
                    tank.get_events()  # 在键盘事件中射击子弹
                    tank.move()
                    # 显示子弹
                    for bullet in tank.bullet_list:
                        if bullet.live:
                            bullet.display_bullet(MainGame.window)
                            bullet.bullet_move()
                            bullet.hit_enemy_tank()
                        else:
                            tank.bullet_list.remove(bullet)
                else:
                    self.players.remove(tank)

            # 显示敌方tank
            for tank in self.enemy_tanks:
                if tank.live:
                    tank.display_tank(MainGame.window)
                    tank.random_move()
                    # 射击子弹
                    name = "enemy_missile"
                    speed = tank.speed + 1
                    # speed = 2
                    tank.random_shot(name, speed)
                    # 显示子弹
                    for bullet in tank.bullet_list:
                        if bullet.live:
                            bullet.display_bullet(MainGame.window)
                            bullet.bullet_move()
                            bullet.hit_my_tank()
                        else:
                            tank.bullet_list.remove(bullet)
                else:
                    self.enemy_tanks.remove(tank)

            # 显示爆炸效果
            for explode in self.explode_list:
                if explode.live:
                    explode.display_explode(MainGame.window)
                else:
                    self.explode_list.remove(explode)

            # 刷新
            pygame.display.update()
            time.sleep(0.01)

    # 结束游戏
    def end_game(self):
        print("Thanks your time")
        # 结束python解释器
        exit()

    # 添加文字说明
    def get_text_surface(self, text):
        pygame.font.init()
        font = pygame.font.SysFont("kaiti", 18)
        text_surface = font.render(text, True, MainGame.COLOR_RED)
        return text_surface

    # 创建我方tank
    def create_mytanks(self, count):
        for i in range(count):
            top, left = 550,  (2*(i+1)-1)*(self.screen_width/4)  # tank的出现位置
            my_player = MyTank(self, "mytank"+str(i+1), MainGame.player_speed, left, top, i+1)
            self.players.append(my_player)

    # 创建敌方tank
    def create_enemytank(self, count):
        for j in range(count):
            for i in range(3):  # 三种敌方tank，每种数量为count
                enemy = EnemyTank(self, "enemy"+str(i+1))
                self.enemy_tanks.append(enemy)


if __name__ == "__main__":
    MainGame().start_game()
