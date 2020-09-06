"""
原型模式（Prototype）: 通过原型模式拷贝出一个新的对象

使用场景：
通过动态装载； 为了避免创建一个与产品类层次平行的工厂类层次时；
当一个类的实例只能有几个不同状态组合中的一种时。建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。

动态装载（英语：Dynamic Loading）是一种程序运行机制，能让计算机程序在运行时（而不是编译时）装载库（或者其他二进制对象）到内存中，
然后检索库中函数和变量的地址，并运行这些函数或访问这些变量，且能在不需要时将库从内存中卸载。

"""

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    # 克隆已注册的对象并更新内部属性字典
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        print(obj.__dict__, obj, id(obj))   # a 是 新对象
        obj.__dict__.update(attr)

        return obj

def main():
    class A:
        def __str__(self):
            return "I am A"


    a = A()
    print(id(a))
    prototype = Prototype()

    prototype.register_object('a', a)   # 创建一个对象

    b = prototype.clone('a', a=1, b=2, c=3)    #

    print(b.__dict__)    # 还是 a 对象

    print(b.a, b.b, b.c)

if __name__ == '__main__':
    main()




