class Cat:  # 定义类
    def eat(self):  # 定义对象方法
        print("吃东西")

# 创建对象
tom = Cat()
# 调用对象方法
tom.eat()
# 定义属性和变量类似  首次赋值会定义对象属性  对象名.属性名 = 数据
tom.type = "猫"
# 访问对象属性  对象名.属性名
print(tom.type)
# 再次赋值,只会修改属性记录的数据
tom.type = "电影明星"
print(tom.type)