# 单例模式： 保证一个类只有一个实例，并提供一个访问它的全局访问点

# __init__ 回去 调用 __new__方法 创建一个实例

from abc import abstractmethod, ABCMeta

# 1. 使用__new__方法
class Singleton:
    # __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):    #如果对象有该属性返回 True，否则返回 False。
            # print(cls)
            # super().xxx 代替 super(Class, self).xxx  调用父类方法
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls

class MyClass(Singleton):

    # __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值
    # 构造方法
    def __init__(self):
        pass


# class MyClass2:
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):    #如果对象有该属性返回 True，否则返回 False。
#             # super().xxx 代替 super(Class, self).xxx  调用父类方法
#             cls._instance = super().__new__(cls)
#
#         return cls
#
#     # __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值
#     # 构造方法
#     def __init__(self):
#         print('init')


a = MyClass(10)
print(MyClass._instance)
b = MyClass(20)
print(id(a), id(b), id(Singleton), id(MyClass))
print(a.mro())   # 打印类的继承关系


# 2. 装饰器方法
def singleton(cls, *args, **kw):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance

@singleton
class MyClass2:
    a = 1

one = MyClass2()
two = MyClass2()

print(id(one))
print(id(two))
print(one == two)
print(one is two)



# 3.import 方法

# Python的模块是天然的单例模式。
class MySingleton(object):
    def foo(self):
        print('单例')

my_singleton = MySingleton()


# 4.使用metaclass

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

# python2
# class MyClass:
#     __metaclass__ = Singleton

# python3
class MyClass(metaclass=Singleton):
    pass

a = MyClass()
b = MyClass()

print(id(a), id(b))



