class SweetPotato:
    """地瓜类"""
    def __init__(self):
        # 定义属性
        self.state = "生的"  # 烧烤状态
        self.cooked_time = 0  # 烧烤总时间

    def __str__(self):
        return "地瓜的状态:%s, 烧烤的总时间:%d" % (
            self.state, self.cooked_time)

    def cook(self, time):
        """烧烤"""
        # 累加求出烧烤总时间
        self.cooked_time += time
        # 根据总时间,设置地瓜的状态
        if self.cooked_time >= 0 and self.cooked_time < 3:
            self.state = "生的"
        elif self.cooked_time >= 3 and self.cooked_time < 6:
            self.state = "半生不熟"
        elif self.cooked_time >= 6 and self.cooked_time < 8:
            self.state = "熟了"
        else:
            self.state = "烤糊了"

digua1 = SweetPotato()
digua1.cook(2)
print(digua1)
digua1.cook(2)
print(digua1)
digua1.cook(3)
print(digua1)