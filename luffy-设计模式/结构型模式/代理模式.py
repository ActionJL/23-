# 租房   中介就是房东的代理。   访问服务器上网,代理服务器    我 通过 代理服务器 访问 服务器上网
"""
应用场景
远程代理 ：ORM
虚代理 ：根据需要访问一个很大对象
保护代理 ：普通用户只有读的权限
"""


# 如何实现？

# 代理一个东西，首先得要有这个东西

from abc import ABCMeta, abstractmethod

# 主题是 操作文件
# 接口的目的是为了有真实的物体，和代理的物体， 为了让真实和代理物体对外表现是一样的。
# 抽象实体： 目的就是为了是 真实对象 和 代理对象 对外具有一致的方法。目的是为何使高层代码可以统一使用。
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):   # 获取内容
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()

# subject= RealSubject('test.txt')   # 如果不用虚代理，在创建这个对象时，已经就会将文件读取进来了
# subject.get_content()    # 后面即使用户不执行该句， content也会一直占在内存

# 虚代理 > 只有调用 get_content（）, 才真实的调用 RealSubject.
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)

        return self.subj.get_content()

    def set_content(self, content):
        return self.subj.set_content()

# 依旧读取文件内容
# subject= RealSubject('test.txt')
# subject.get_content()

subj = VirtualProxy('test.txt')    # 不会打印读取文件内容， 说明没有占内存
# print(subj.get_content())   # 只有执行这句才会去读取文本信息

# 虚代理： 节省内存开销


# 保护代理 > 只有读权限，没有写权限，就可以整个保护代理
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")


subj = ProtectedProxy('test.txt')
print(subj.get_content())
# subj.set_content("abc")

"""
角色：
抽象实体（Subject）
实体（RealSubject）
代理（Proxy）

优点：
远程代理：可以隐藏对象位于远程地址空间的事实
虚代理：可以进行优化，例如根据要求创建对象
保护代理：允许在访问一个对象时有一些附加的内务处理

"""