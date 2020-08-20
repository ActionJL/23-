def a(x):

    def b():
        pass

    def c():
        pass

    if x=='b':
        return b
    else:
        return c

print(a.__name__)

@a
def d():
    pass

#
# 如何通过调用a() ， 执行b()或c()
#
# 装饰器核心：函数名可以通过变量进行传递
# 装饰器：函数嵌套函数
# 上方运行原理： 把d函数名作为参数传递给a函数
#
# __call__()的作用是使实例能够像函数一样被调用，同时不影响实例本身的生命周期（__call__()不影响一个实例的构造和析构）。
# 但是__call__()可以用来改变实例的内部成员的值。
#
# # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#
#
# 类也可以实现装饰器， 说白了就是采用 __call__方法， 是实例可以向函数一样被调用。