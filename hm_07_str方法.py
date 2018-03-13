class Cat:
    def __init__(self):
        self.type = "猫"

    def __str__(self):  # 魔法方法:会在特定情况下自动调用
        # str方法 会在 print(对象) 时 自动调用
        # str方法返回值为什么, print就会打印什么
        # 返回值必须为字符串
        return "类型为%s" % self.type

tom = Cat()
print(tom)