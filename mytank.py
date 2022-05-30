import pygame
from tank import Tank


class MyTank(Tank):
    def __init__(self, main_game, name, speed, left, top, player=None):
        super().__init__(main_game, name, speed, left, top)
        self.player = player

    # 碰撞敌方坦克的方法
    def hit_enemy_tank(self):
        pass

    # 添加键盘事件
    def get_events(self):
        # 获取所有事件
        event_list = pygame.event.get()
        # 判断事件
        for event in event_list:
            # 退出事件
            if event.type == pygame.QUIT:
                self.main_game.end_game()
            # 按键事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # print("坦克向左调头，移动")
                    self.direction = "L"
                    # self.move()
                    self.stop = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # print("坦克向右掉头，移动")
                    self.direction = "R"
                    # self.move()
                    self.stop = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # print("坦克向上掉头，移动")
                    self.direction = "U"
                    # self.move()
                    self.stop = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # print("坦克向下掉头，移动")
                    self.direction = "D"
                    # self.move()
                    self.stop = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_u:
                    # print("发射子弹")
                    img_name = "my_missile"
                    speed = 4
                    self.shot(img_name, speed)

            # 松开的如果是方向键，才更改移动开关状态
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a \
                        or event.key == pygame.K_RIGHT or event.key == pygame.K_d \
                        or event.key == pygame.K_UP or event.key == pygame.K_w \
                        or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # 修改坦克的移动状态
                    self.stop = True
