# 类似于抽象工厂模式， 不仅要生产一套，还要控制生产顺序。

# 游戏的角色建模
from abc import ABCMeta, abstractmethod

# 产品
class Player:
    # 角色的四部分组成
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %sm, %s, %s" % (self.face, self.body, self.arm, self.leg)


# 工厂 在建造者中，叫Builder
# 构造代码
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

# 对于每一个具体工厂，我们可以生成一套具体产品
#
class SexyGirlBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()    # 首先得加一个玩家

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '大胳膊'

# 怪兽
class MonsterBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()  # 把玩家返回出去

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽苗条"

    def build_arm(self):
        self.player.arm = '怪兽胳膊'

    def build_leg(self):
        self.player.leg = '长毛的腿'

# 控制着，导演   控制组装顺序
# 装配代码
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client

builder = SexyGirlBuilder()

director = PlayerDirector()

p = director.build_player(builder)

print(p)


"""
建造者模式与抽象工厂模式相似，也用来创建复杂对象。
主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。
优点：
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制 

"""