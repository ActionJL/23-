"""
1. 适配器模式（Adapter Class/Object）
内容：将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
角色：

目标接口（Target）
待适配的类（Adaptee）
适配器（Adapter）
两种实现方式：
类适配器：使用多继承
对象适配器：使用组合

适用场景：
想使用一个已经存在的类，而它的接口不符合你的要求
（对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

类适配器：
用一个具体的Adapter类对Adaptee和Target进行匹配。结果是当我们想要匹配一个类以及所有他的子类时，类Adaptee将不能胜任工作。
使得Adapter可以重定义Adaptee的部分行为，因为Adapter是Adaptee的一个子类。
仅仅引入一个对象，并不需要额外的指针以间接得到Adaptee。

对象适配器：
允许一个Adapter与多个Adaptee——即Adaptee本身以及它所有的子类（如果有子类的话）一同时工作。Adapter也可以一次给所有的Adaptee添加功能。
使得重定义Adaptee的行为比较困难。这酒需要生成Adaptee的子类并且使得Adapter引用这个子类而不是引用Adaptee本身。
"""



from abc import abstractmethod, ABCMeta

# 目标接口
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









