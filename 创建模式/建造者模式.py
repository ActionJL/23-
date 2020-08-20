from abc import abstractmethod, ABCMeta

# 产品
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.arm, self.body, self.leg)

# 抽象建造者
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def get_player(self):
        pass

# 具体建造者
class BeautifulWomanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_arm(self):
        self.player.arm = "细胳膊"

    def build_body(self):
        self.player.body = "细腰"

    def build_leg(self):
        self.player.leg = "长腿"

    def get_player(self):
        return self.player

# 指挥者
class PlayerDirector:

    def builder_player(self, builder):
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        builder.build_face()

        return builder.get_player()


director = PlayerDirector()
builder = BeautifulWomanBuilder()
p = director.builder_player(builder)
print(p)


