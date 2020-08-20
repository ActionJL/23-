# 抽象方法：
# 抽象方法表示基类的一个方法，没有实现，所以基类不能实例化，子类实现了该抽象方法才能被实例化。

from abc import ABC, abstractmethod


class Foo(ABC):
    @abstractmethod
    def fun(self):
        '''please Implemente in subclass'''


class SubFoo(Foo):
    # 这个方法必须有，否则无法实例化
    def fun(self):
        print('fun in SubFoo')

a = SubFoo()
a.fun()