# 策略模式： 定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化

# 约车服务 > 滴滴    人打车，司机评分，司机与人之间距离，价格 等等
# 给一个乘客位置，根据一个位置，来匹配一个司机给他  >   这是一个策略
# 算法1 效果好，运行慢
# 算法2 运行快，效果一般
# 高峰期，用算法2，快一些。 低峰期，用算法1，体验好。 像这种策略的切换，我们封装起来，就是我们的策略模式



from abc import ABCMeta,abstractmethod

#策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

class FastStratege(Strategy):
    def execute(self, data):
        print("用较快的策略处理 %s" , data)

class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理 %s", data)

#作用：再封装一层，把策略+数据通过上下文传进去。
class Context:
    def __init__(self, strategy, data):
        self.data = data
        # self.date = datetime.now()    策略模式：也可以向用户隐藏一些信息。 如这行代码
        self.strategy = strategy

    def set_strategy(self, strategy):   # 切换策略
        self.strategy = strategy

    def do_strategy(self):    # 执行策略
        self.strategy.execute(self.data)


# Client
data = "[...]"
s1 = FastStratege()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()

context.set_strategy(s2)
context.do_strategy()


"""
抽象策略（Strategy）
具体策略（ConcreteStrategy）
上下文（Context） 


优点：
定义了一系列可重用的算法和行为
消除了一些条件语句
可以提供相同行为的不同实现

缺点：
客户必须了解不同的策略 

"""