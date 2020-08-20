# 2. 工厂方法模式（Factory Method）
#
# 内容：定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。
#
# 角色：
#
# 抽象工厂角色（Creator）
# 具体工厂角色（Concrete Creator）

# 抽象产品角色（Product）
# 具体产品角色（Concrete Product）

from abc import abstractmethod, ABCMeta

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class ApplePay(Payment):
    def pay(self, money):
        print('苹果支付%s元'%money)

af = ApplePayFactory()
apay = af.create_payment()
apay.pay(100)