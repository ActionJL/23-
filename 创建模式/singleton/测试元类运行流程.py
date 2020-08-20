class Mymeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('===>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('===>Mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('===>Mymeta.__call__')
        print(self)
        obj = self.__new__(self)
        self.__init__(self, *args, **kwargs)
        return obj



class Foo(metaclass=Mymeta):

    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)



# foo = Foo('foo')

# 抽象类中的方法都是抽象方法，必须要有子类去实现
# 有抽象方法的类不一定是抽象类

'''

在没有 metaclass 的情况下，子类继承父类，父类是无法对子类执行操作的，
但有了 metaclass，就可以对子类进行操作，就像装饰器那样可以动态定制和修改被装饰的类，
metaclass 可以动态的定制或修改继承它的子类。




从上面的运行结果可以发现在定义 class Foo() 定义时，
会依次调用 MyMeta 的 __new__ 和 __init__ 方法构建 Foo 类，
然后在调用 foo = Foo() 创建类的实例对象时，
才会调用 MyMeta 的 __call__ 方法来调用 Foo 类的 __new__ 和 __init__ 方法。


把上面的例子运行完之后就会明白很多了，正常情况下我们在父类中是不能对子类的属性进行操作，但是元类可以。
换种方式理解：元类、装饰器、类装饰器都可以归为元编程

'''