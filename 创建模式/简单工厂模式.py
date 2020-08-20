# 简单工厂模式： 不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例

# 工厂角色   PaymentFactory
# 抽象产品角色   Payment
# 具体产品角色

# 优点： 隐藏了对象创建的实现细节， 客户端不需要修改代码

# 缺点：违反单一职责原则， 添加新产品需要改PaymentFactory违反了开闭原则

# 创建一个对象的时候
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):

    def __init__(self,use_huabei):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('huabei支付%d元' % money)
        else:
            print('支付宝支付%d元' % money)

class WechatPay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)

class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei = True)
        else:
            raise TypeError('No such payment named %s' % method)



# client

# pf = PaymentFactory()
# p = pf.create_payment('huabei')
# p.pay(100)

################################################################
# 1. 简单工厂模式
# 内容：定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。

# 角色：
# 工厂角色（创造支付产品）
# 抽象产品角色（支付产品）
# 具体产品角色（苹果支付，花呗支付，支付宝支付）


from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class ApplePay(Payment):
    def pay(self, money):
        print('苹果支付%s元'%money)

class PaymentFactory:
    def create_payment(self, method):
        if method == 'applepay':
            return ApplePay()
        else:
            raise NameError(method)

f = PaymentFactory()
p = f.create_payment('applepay')
p.pay(100)













