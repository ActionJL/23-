# 什么是抽象方法？
class Alipay:
    def pay(self, money):
        pass

class WechatPay:
    def pay(self, money):
        pass


p = Alipay()
p.pay(100)





from abc import ABCMeta, abstractmethod

'''
接口作用： 限制实现接口的类必须按照接口给定的调用方式实现这些方法。

对高层模块隐藏了类的内部实现

底层模块

抽象类  abstract class
    
'''
# 方式一： 存在问题就是  只执行 p = Alipay() 不会抛出异常
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError


# 方式二： 抽象方法， 约束子类必须实现该方法。
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


# 一般叫  实现接口
# 底层模块 > 可以将设计模式用的贼溜

