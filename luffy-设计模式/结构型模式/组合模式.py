# 组合模式： 将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。
# 怎么理解呢？
# 如PPT画图中 > 组成功能   正方形+圆形     圆形     复杂对象 和 简单对象 都有 剪切 删除等功能

from abc import ABCMeta, abstractmethod

# 因为对他们使用具有一致性，所以得有一个统一的接口。
# 怎样让部分和整体的对象使用具有一致性？ 就是提供一个统一的接口，让他们两个(简单对象和复杂对象)都有这种方法，操作一致
# 定义一个接口

# 抽象组件 ： 保证叶子组件和复合组件 都有公共的方法。
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):   # 都要有绘制
        pass

    # @abstractmethod
    # def copy(self):
    #     pass

# 两种简单对象  >  叶子组件
# 点
# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点（%s , %s）" % (self.x, self.y)

    def draw(self):
        print(str(self))

# 线
# 叶子组件
class  Line(Graphic):
    def __init__(self, p1, p2):  # 由两个点组成
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))

# 复杂对象
# 复合组件： 由多个叶子组件组成
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []   # 父  就是记录孩子节点
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("----复合图形----")
        for g in self.children:
            g.draw()
        print("----复合图形----")

# 客户端： 就是调用代码

l = Line(Point(1,1), Point(2,2))
print(l)

#
p1 = Point(2,3)
l1 = Line(Point(3,4), Point(6,7))
l2 = Line(Point(1,5), Point(2,8))

pic1 = Picture([p1, l1, l2])
pic1.draw()

print('-'*50)

p2 = Point(4,4)
l3 = Line(Point(1,1), Point(0,0))
pic2 = Picture([p2, l3])

pic = Picture([pic1, pic2])
pic.draw()

"""
抽象组件（Component）
叶子组件（Leaf）
复合组件（Composite）
客户端（Client）

适用场景：
表示对象的“部分-整体”层次结构（特别是结构是递归的）   > draw 是递归
希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象  > 对外是一样的

优点：
定义了包含基本对象和组合对象的类层次结构
简化客户端代码，即客户端可以一致地使用组合对象和单个对象
更容易增加新类型的组件

"""