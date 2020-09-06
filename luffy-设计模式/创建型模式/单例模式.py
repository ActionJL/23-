# 单例模式： 保证一个类出来的实例只有一个

# python的模块就是单例， 当然模块不是对象

# 基类
class Singleton:
    # 重写__new__方法
    # __new__方法的作用：在面向对象的时候， 会在init之前，给整个对象进行初始化，分配空间等等
    # 类方法：可直接类名调用
    def __new__(cls, *args, **kwargs):
        # 用一个类属性，来表示类的实例，如果类有这个属性，那么直接返回实例

        # super().xxx 代替 super(Class, self).xxx
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)   # cls可能是未来的类名

        return cls._instance


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a     # 作用： 验证是否同一实例

a = Myclass(10)
b = Myclass(20)

print(a.a, b.a)    # 输出都是20 ， 说明是同一个实例

print(id(a), id(b))

# 应用场景： 日记对象， 数据库连接器， 文件系统， 计数。 只有一个实例能存在，那就用单例
"""

内容：保证一个类只有一个实例，并提供一个访问它的全局访问点。


角色：
单例（Singleton）

优点：
对唯一实例的受控访问
单例相当于全局变量，但防止了命名空间被污染

什么叫防止命名空间被污染？
就是说可以采用全部变量来实现单例模式，但是全局变量一旦定义，整个全局都得用它。一改动就会存在问题。 而这里就不会存在这种问题，a, b随意用。

"""
