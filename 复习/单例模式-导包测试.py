
import numpy as np
print(id(np))


i = 0
while i<100:
    import numpy as np
    print(id(np))
    i += 1

if __name__ == '__main__':
    # class()
    pass