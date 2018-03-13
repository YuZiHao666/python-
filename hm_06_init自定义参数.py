class Cat:
    def __init__(self, name, type):
        """初始化方法 专门用于做一些对象的初始操作(如 定义属性)"""
        # 想让属性拥有不同的初始值时,可以设置init的自定义参数
        self.type = type  # 类型
        self.name = name  # 姓名

    def introduce(self):
        print("我是%s, 你好" % self.type)

tom = Cat("汤姆", "明星")  # init自定义参数对应的实参在创建对象时设置:  类名(实参)
print(tom.name)
tom.introduce()

jiafei = Cat("加菲", "漫画人物")
print(jiafei.name)
jiafei.introduce()
