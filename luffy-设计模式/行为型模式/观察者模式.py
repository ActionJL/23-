# 观察者模式 又被称为 发布-订阅模式。
# 定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。观察者模式又称“发布-订阅”模式
# 订阅者 就是 观察者。

"""
重点：
在设计模式中，观察者模式着重在什么地方？
1.发布者的状态发生变化，这些订阅者都自动被更新。 而不需在高层手动去更新，需要判断他是订阅他，手动去更新。
2.发布者 和 订阅者 是一个松耦合， 也就是 可以取消订阅。

"""

# 如何实现观察者模式？

# 拿一个 消息中心 + 订阅

# 根据依赖元素，定义约束关系，针对接口编程

from abc import ABCMeta,abstractmethod

# 观察者   抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):    # notice 是一个 Notice类的对象
        # 有一个发布者的状态发生变化的时候, 观察者就得根据发布者最新状态进行更新
        pass


# 发布者
class Notice:
    def __init__(self):
        self.observer = []

    # 有哪些订阅
    def attach(self, obs):
        self.observer.append(obs)

    def detach(self, obs):
        self.observer.remove(obs)

    # 发布者状态发生变化，应该通知所有观察者
    # 通知
    def notify(self):    # 推送
        for obs in self.observers:
            obs.update(self)   # 将Notice对象传入


# 具体订阅者 发布者


# 具体发布者 --- 公司公告
class StaffNotice(Notice):
    def __init__(self, company_info):
        super().__init__()
        self.__company_info = company_info    # 为什么做成私有？

    # 属性装饰器
    @property
    def company_info(self):
        return self.__company_info

    # 写
    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()    # 目的：推送，推送给所有观察者。  把订阅者的company_info绑定在自己身上。


# 复习 属性装饰器
obj = StaffNotice("abc")
# obj.__comany_info   # 私有在内外无法访问
obj.company_info = "xyz"   # 动态跳转到 def company_info(self, info) 这个方法
print(obj.company_info)   # 而将方法定义为属性，该句直接跳转到  def company_info(self) 这个方法. 从而将属性打印出。



# 具体订阅者  ---  员工
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info



# Client
notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)

# 修改
notice.company_info = "公司今年业绩非常好，给大家发奖金"    # 只把发布者的信息改了
print(s1.company_info)
print(s2.company_info)


notice.detach(s2)
notice.company_info = "公司明天放假！！"
print(s1.company_info)
print(s2.company_info)


"""
角色：
抽象主题（Subject）   >    Observer   Notice
具体主题（ConcreteSubject）——发布者    >   StaffNotice
抽象观察者（Observer）  > Observer
具体观察者（ConcreteObserver）——订阅者    >  Staff


适用场景：
当一个抽象模型有两方面，其中一个方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用。
当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象有待改变。
当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之，你不希望这些对象是紧密耦合的。

优点：
目标和观察者之间的抽象耦合最小
支持广播通信 


"""