# 3. 抽象工厂方法（Abstract Factory）
# 内容：定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
# 例：生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，分别生产一部手机所需要的三个对象。
# 角色：
#
# 抽象工厂角色（Creator）
# 具体工厂角色（Concrete Creator）
# 抽象产品角色（Product）
# 具体产品角色（Concrete Product）
# 客户端（Client）
# 相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。

from abc import abstractmethod, ABCMeta

# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        print('小手机壳')

class BigShell(PhoneShell):
    def show_shell(self):
        print('大手机壳')

# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass


# 具体工厂
class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

class IPhoneFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

# 客户端
class Phone:
    def __init__(self, shellObj):
        self.shellObj = shellObj

    def show_info(self):
        print('手机信息：')
        self.shellObj.show_shell()

def make_phone(factory):
    shellObj = factory.make_shell()
    return Phone(shellObj)

p1 = make_phone(HuaweiFactory())
p1.show_info()









