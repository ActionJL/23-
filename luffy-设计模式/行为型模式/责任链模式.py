# 什么是责任链模式？
# 使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。
# 将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

"""
比如 在系统中提出一个请求， 爬虫爬到一条数据，或者由某个用户发起一个请求，这个请求需要处理.
系统中可能有多个对象去处理这些请求，那么怎么样保证这个请求动态的应该被谁处理。 这样一个事情， 把请求的接受者连成一条链，这条链就称之为责任链。

再比如
公司请假 >  leader 可签你2天假，高一点就得部门经理签了。 部门经理 可签5天。总经理 可签10天。 程序跑起来，根据权限决定程序由谁来处理。
为了避免假期 和 处理假期的人之间的强耦合，因此引入责任链模式。 否则如果在高层代码中实现判断，有几天假，给leader处理，万一leader可签5天了，那么代码将改变好多。

"""

# 如何来实现责任链模式呢？   # 链表模式

# 来几个请求处理者
# 接口
# 底层代码 + 配置责任链的过程
from abc import ABCMeta, abstractmethod


class Handler(metaclass = ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

# 总经理
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假 %d 天" % day)
        else:
            print("你还是辞职吧")

# 部门经理
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假 %d 天" % day)
        else:
            print("部门经理职权不足")


# 项目主管
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 1:
            print("项目主管准假 %d 天" % day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)


# 高层代码 > 不需要知道是谁处理。   具体应用： Scrapy  pipeline
# client

day = 4

h = ProjectDirector()
h.handle_leave(day)


"""
内容：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

角色：
抽象处理者（Handler）
具体处理者（ConcreteHandler）
客户端（Client）


适用场景：
有多个对象可以处理一个请求，哪个对象处理由运行时决定
在不明确接收者的情况下，向多个对象中的一个提交一个请求

优点：
降低耦合度：一个对象无需知道是其他哪一个对象处理其请求

"""