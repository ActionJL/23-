# 桥模式： 比如说画图程序， 画图程序就应该要有形状 直线，圆，长方形等 ，每种形状要灼上颜色。
# 桥模式：将一个事物的两个维度分离，使其都可以独立的变化。

# 这就是一个事物的两个维度   形状  颜色，两个维度是独立的， 两个维度必须都有才能形成这种事物。

# 如何通过代码来实现 两个维度分离， 两个维度独立？

# 方式1
from abc import ABCMeta, abstractmethod


class Shape:
    pass

class Line(Shape):
    pass

#长方形
class Rectangle(Shape):
    pass

# 圆
class Circle(Shape):
    pass

class RedLine(Line):
    pass

class GreenLine(Line):
    pass

class BuleLine(Line):
    pass

# 以上方式可以，不过不容易扩展， 加一个形状，加一个颜色，需改很多代码。

# 如何解决呢？ 利用设计模式的桥模式

# 定义形状类
# 抽象
class Shape(metaclass=ABCMeta):    # Shape 接口 指的就是在形状下有什么表现
    # 在构造函数中  将color传入， 把color作为shape的一个属性。
    # 形状和颜色 就可以通过 组合的方式进行耦合
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):    # 画图
        pass
# 实现
class Color(metaclass=ABCMeta):    # Color 给一个图形画上一个颜色
    @abstractmethod
    def paint(self, shape):    #paint 灼上
        pass

# 如何将 Shape  Color 关联起来呢？   组合方式
# 为什么不用继承呢？ 因为继承是紧耦合。

# 具体类  长方形
class Rectangle(Shape):   # 长方形 实现  Shape
    name = '长方形'
    def draw(self):    # 长方形是在形状维度   self 是形状 Rectangle
        # 长方形逻辑
        self.color.paint(self)    # 实现画图起来需要颜色来实现，那么就需要用color的paint函数

class Circle(Shape):
    name = '圆形'
    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)

class Green(Color):
    def paint(self, shape):
        print("绿色的 %s" % shape.name)


# 高层代码
# 画一个红色长方形

shape = Rectangle(Red())   # 目的就是 将color对象 放入到 shape类中去了
shape.draw()    #

shape2 = Circle(Green())
shape2.draw()

# 现在增加一个图形 和 一种颜色
class Triangle(Shape):
    name = '三角形'
    def draw(self):
        self.color.paint(self)

class Blue(Color):
    def paint(self, shape):
        print("蓝色的 %s" % shape.name)

shape3 = Triangle(Blue())
shape3.draw()

# 形状的 > draw方法， 调用颜色中的 > paint方法
"""
抽象（Abstraction）   >  形状
细化抽象（RefinedAbstraction）  > 长方形， 圆形

实现者（Implementor）   > 颜色
具体实现者（ConcreteImplementor）  > 红  绿   蓝


应用场景：  如开发桌面程序框架  维度1： 窗口类  单文档窗口，多文档窗口。 维度2： 操作系统 >  linux 系统  window系统 也是两个维度
当事物有两个维度上的表现，两个维度都可能扩展时。

优点：
抽象和实现相分离
优秀的扩展能力

"""