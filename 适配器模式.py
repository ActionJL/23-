from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元" % money)


# ------待适配类------

class WechatPay:
    def cost(self, money):
        print("微信支付%s元" % money)


# 类适配器
class RealWechatPay(WechatPay, Payment):
    def pay(self, money):
        return self.cost(money)


# 对象适配器

class RealWechatPay2(Payment):
    def __init__(self):
        self.payment = WechatPay()

    def pay(self, money):
        return self.payment.cost(money)


p = RealWechatPay2()
p.pay(111)