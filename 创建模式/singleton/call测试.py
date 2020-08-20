class Mymeta:
    def __init__(self):
        print('===>Mymeta.__init__')

    def __call__(self, *args, **kwargs):
        print('===>Mymeta.__call__')


Mymeta.__call__(Mymeta())