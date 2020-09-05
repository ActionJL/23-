from abc import ABCMeta, abstractmethod

'''
接口作用： 限制实现接口的类必须按照接口给定的调用方式实现这些方法。

对高层模块隐藏了类的内部实现

底层模块

抽象类  abstract class
    
'''
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        pass


class WechatPay(Payment):
    def pay(self, money):
        pass


# 高层模块
p = Alipay()
p.pay(100)







