# 开放封闭原则


# 里氏替换原则 : 说白了就是 同一个 show_name 返回值一致
from abc import abstractmethod, ABCMeta


class User:
    def show_name(self):
        pass

class VIPUser(User):
    def show_name(self):
        pass

u = User()
res = u.show_name()


# 高层函数
def show_user(u):
    res = u.show_name()



# 依赖倒置原则: 针对接口编程
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


# 高层模块
p = Alipay()
p.pay(100)


# 接口隔离原则
"""
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Tiger(Animal):
    def walk(self):
        print('老虎走路')

    # def swim(self):
    #     print('老虎游泳')
    #
    # def fly(self):
    #     print('老虎不会飞')

t = Tiger()  # Can't instantiate abstract class Tiger with abstract methods fly, swim
# 不要使用单一的总接口， 使用多个专门的接口，更改如下    陆地动物   水里动物    天数动物
"""

class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print('老虎走路')

t = Tiger()


# 单一职责原则： 一个类只负责一项职责
