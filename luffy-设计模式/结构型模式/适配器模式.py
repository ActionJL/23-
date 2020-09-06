# 结构型模式： 几个类在一起协同工作
# 适配器模式： 加一个适配器，使两个类能在一起工作

from abc import ABCMeta, abstractmethod

# 抽象 : 目的是使 产品 有同样的表现，可以同样的对待使用。
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 产品
class Alipay(Payment):
    def pay(self, money):
            print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


p = Alipay()
p.pay(100)


##
class BankPay:
    def cost(self, money):
        print("银联支付%d元" % money)

# 报异常， 假设是两个系统合并为一个系统，如何才能兼容呢？ 适配器模式
# p = BankPay()
# p.pay(100)

# 解决方式一：   类适配器 > 他能将本来不兼容的接口cost, 转成兼容的接口pay.   （使用的是多继承）
class NewBankPay(Payment, BankPay):
    # 实现Payment目的是为了使接口统一， 继承BankPay的目的是为了复用代码
    def pay(self, money):
        self.cost(money)   #参数个数，顺序可在这调整

p = NewBankPay()
p.pay(100)

# 问题: 假如有好几个类都有问题，怎么办？
# 再来一个,假如有多个类似cost的类。 就不能用上方方式，每个都来继承一下。用组合方式
class ApplePay:
    def cost(self, money):
        print("苹果支付%d元" % money)

# 解决方式二： 对象适配器 > 通过组合方式完成的代码复用。
# 适配器的目的是什么？  1. 与接口保持一致（实现接口）  2.复用代码(继承+组合)
# 面向对象复用代码两种方式： 继承 + 组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment
    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p = PaymentAdapter(BankPay())
p.pay(100)


# 组合: 在一个类中，放入另一个类的对象
class A:
    pass
class B:
    def __init__(self):
        self.a = A()


"""
角色：
目标接口（Target）
待适配的类（Adaptee）
适配器（Adapter）

适用场景：
想使用一个已经存在的类，而它的接口不符合你的要求
（对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。 

"""