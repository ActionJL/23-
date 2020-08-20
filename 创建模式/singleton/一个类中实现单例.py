
class Singleton():

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)

        return cls._instance


    def __init__(self, n):
        self.n = n

a = Singleton(2)
b = Singleton(3)

print(a.n, b.n)