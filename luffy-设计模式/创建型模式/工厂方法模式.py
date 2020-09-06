from abc import ABCMeta, abstractmethod

# 抽象 : 目的是使 产品 有同样的表现，可以同样的对待使用。
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 产品
class Alipay(Payment):
    def __init__(self, use_huabei = False):
        self.use_huabei = use_huabei


    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)

# 加一个产品 银联支付
class BankPay(Payment):
    def pay(self, money):
        print('银联支付 %d 元' % money)



# 简单工厂模式 将好几种产品的创建逻辑集中在一个工厂，现在拆开， 一个工厂生产一个产品。
# 工厂接口
class PaymentFactory(metaclass = ABCMeta):    # 工厂类需要哪些方法？ 创建对象 create_payment这个抽象方法
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


# 对应的增加一个银联工厂类即可。   代码 28--57 行，之前代码没有改, 之前的逻辑没哟变。 创建一个产品的时候， 创建对应的工厂模式即可。
class BankFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# client

pf = HuabeiFactory()
p = pf.create_payment()    # 直接调用就行
p.pay(100)

# 单一职责原则

"""

优点：
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
隐藏了对象创建的实现细节

缺点： 代码变多了
每增加一个具体产品类，就必须增加一个相应的具体工厂类

"""