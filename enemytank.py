import random

from tank import Tank


class EnemyTank(Tank):
    def __init__(self, main_game, name):
        speed = random.randint(1, 3)
        left = 100 * random.randint(1, 7)
        top = 100
        super().__init__(main_game, name, speed, left, top)
        self.direction = self.rand_direction()
        self.stop = False
        self.step = 50  # tank 50步后改变发方向

    # 重写shot方法，随机发射子弹
    def random_shot(self, name, speed):
        num = random.randint(1, 1000)
        if num <= 20:
            self.shot(name, speed)

    # 随机移动 每走step步就改变方向
    def random_move(self):
        if self.step <= 0:
            self.direction = self.rand_direction()
            self.step = random.randint(5, 60)
        else:
            self.move()
            self.step -= 1

    # 碰撞我方坦克的方法
    def hit_my_tank(self):
        pass

    # 随机生产4个方向
    def rand_direction(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'
