# 定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类

# 适用场景：
#
# 需要生产多种、大量复杂对象的时候。
# 需要降低耦合度的时候。
# 当系统中的产品种类需要经常扩展的时候。
# 优点：
#
# 每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
# 隐藏了对象创建的实现细节
# 缺点：
#
# 每增加一个具体产品类，就必须增加一个相应的具体工厂类
from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元" % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()


af = AlipayFactory()
ali = af.create_payment()
ali.pay(120)


################################################################
