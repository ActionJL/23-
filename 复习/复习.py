
# 单例模式
class Singleton:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


class Myclass(Singleton):
    def __init__(self,a):
        self.a = a

#
a = Myclass(10)
b = Myclass(20)

print(a.a, b.a)

# 装饰器实现单例模式


def singleton (cls, *args, **kwargs):

    instances = {}

    def get_instance (*args, **kwargs):

        if cls not in instances:

            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance

@singleton
class Myclass2:
    def __init__(self, n):
        self.n = n


a = Myclass2(10)
b = Myclass2(20)

print(a.n, b.n)



# 装饰器，实现单例

def singleton(cls, *args, **kwargs):

    def get_instance(*args, **kwargs):

        if not hasattr(cls, '_instance'):

            cls._instance = cls(*args, **kwargs)

        return cls._instance

    return get_instance


@singleton
class Myclass3:
    def __init__(self, n):
        self.n = n


a = Myclass3(30)
b = Myclass3(40)

print(a.n, b.n)


# 装饰器实现单例模式

def singleton(cls, *args, **kwargs):

    instance = {}

    def get_instance(*args, **kwargs):

        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)

        return instance[cls]

    return get_instance

@singleton
class Myclass4:

    def __init__(self, n):
        self.n = n


a = Myclass4(50)
b = Myclass4(60)
print(a.n, b.n)

#










