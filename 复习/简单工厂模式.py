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