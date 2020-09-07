# 什么叫外观模式呢？
# 为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
'''
说白了 就是 外观模式将电脑的开机工作进行了封装，开机工作需要启动cpu,disk,memory。封装后从而避免调用过程中的漏开启。
如我们忘了启动mysql的某个服务，导致用不了一个意思。
'''

# 子系统类
# 电脑 > CPU  硬盘  内存
# 子系统 > CPU  硬盘  内存
class CPU:
    def run(self):
        print('CPU的运行')

    def stop(self):
        print('CPU停止运行')

class Disk:
    def run(self):
        print('硬盘开始工作')

    def stop(self):
        print('硬盘停止工作')


class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")

# 外观 ： 通过调用子系统类的方法，来完成几个方法的组合。
# 更高级别的系统 > 电脑

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

# client 不需要知道电脑启动是需要运行哪几部分方法，只需通过外观封装的方法即可启用

computer = Computer()
computer.run()
computer.stop()

"""
角色：
外观（facade）   >   封装好的类， 给一组接口提供一致的界面, 几个方法的组合调用，提供了一个高层接口
子系统类（subsystem classes）   >  cpu disk memory

优点：
减少系统相互依赖   >   底层代码 和 高层代码  耦合 依赖 降低。
提高了灵活性
提高了安全性  >  客户端 不需要 去cpu-run  disk-run  mem-run  万一忘了就无法启动了

"""