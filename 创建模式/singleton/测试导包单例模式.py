from 设计模式.single.singleton.single import my_singleton

if __name__ == '__main__':
    my_singleton.foo()
    print(id(my_singleton))
