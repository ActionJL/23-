# 简单工厂模式：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。

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



# 工厂类==生成对象
class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':    # 形象说明客户端不需要了解 底层Alipay的具体实现
            return Alipay(use_huabei = True)
        else:
            raise TypeError('No such payment name %s' % method)



# # 高层模块 == 客户端
# p = Alipay()
# p.pay(100)

# client
pf = PaymentFactory()
# p = pf.create_payment('alipay')
p = pf.create_payment('huabei')    # 直接调用就行
p.pay(100)

"""
优点：
隐藏了对象创建的实现细节
客户端不需要修改代码

缺点：
违反了单一职责原则(管了好多事 即管微信支付，又管支付宝支付，还管花呗支付)，将创建逻辑几种到一个工厂类里
当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""