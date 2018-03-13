class Cat:
    def introduce(self):  # self表示 调用该方法的对象
        """自我介绍"""
        # 在方法中使用对象自己的属性时,使用self来访问
        print("我是%s, 你好" % self.name)
        self.type = "猫"  # 方法中可以定义属性  简化定义属性的过程

# 创建对象
tom = Cat()
tom.name = "汤姆"
tom.introduce()  # python解释器会自动将对象作为第一个实参设置给对象方法
# tom.type = "猫"

# 创建另一个对象
jiafei = Cat()
jiafei.name = "加菲"
jiafei.introduce()
print(jiafei.type)