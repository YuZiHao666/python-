class Cat:
    def __init__(self):  # __xx__ 魔法方法(预定义方法): 这些方法会在特定的情况下自动调用,用于实现一些特定的功能
        """初始化方法 专门用于做一些对象的初始操作(如 定义属性)"""
        # init方法 会在对象一创建完,就立即自动调用
        # 后续的学习和工作中,在init方法中定义对象的属性
        # init方法中定义属性的好处: 1> 避免方法中使用未定义属性而报错  2> 创建的对象都会拥有该属性
        self.type = "猫"

    def introduce(self):
        print("我是%s, 你好" % self.type)

tom = Cat()
tom.introduce()
# tom.type = "猫"

jiafei = Cat()
print(jiafei.type)

