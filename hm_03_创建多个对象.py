class Cat:  # 定义类
    def eat(self):
        print("吃东西")

# 创建一个对象
tom = Cat()
tom.eat()
tom.name = "汤姆"
print(tom.name)

# 利用类可以创建多个对象
jiafei = Cat()
jiafei.eat()  # 同一个类的对象都可以使用对象方法
jiafei.name = "加菲"  # 同一个类的对象可以有同名的属性,而且记录的数据可以不同
print(jiafei.name)