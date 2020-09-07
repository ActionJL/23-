# 内容：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
# 模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

# 模板方法模式： 有好多算法，框架是一样，细节不一样。 父类中框架定义出来，子类去实现该功能。

from time import sleep
from abc import ABCMeta, abstractmethod

# 父类： 实现了一个模板方法， 但是留了很多原子操作/钩子操作。 不便的框架写出来了，便的到子类去实现。
# 定义的是整个系统的框架， 细节未定义
class Window(metaclass=ABCMeta):   # 窗口
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):   # 重新绘制
        pass

    @abstractmethod
    def stop(self):    # 原子操作、钩子操作
        pass

    def run(self):    # 具体方法 这个run方法，就是方法模式中的模板方法。
        self.start()

        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()




# 高层程序员 子类实现

class MyWindow(Window):

    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def repaint(self):  # 重新绘制
        print("窗口重新绘制")

    def stop(self):
        print("窗口停止运行")

MyWindow('Hello').run()

"""
内容：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
角色：
抽象类（AbstractClass）：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架。
具体类（ConcreteClass）：实现原子操作

适用场景：
一次性实现一个算法的不变的部分
各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
控制子类扩展



"""