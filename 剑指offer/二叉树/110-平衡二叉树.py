import gc

import sys


class A:
    pass

class B(list):
    def __del__(self):
        a3.append(self)
        print("del of B")


a1 = A()
a2 = A()

a1.other = a2
a2.other = a1

a3 = list()
b = B()
b.append(b)

d1 = A()
d2 = A()

d1.other = d2
d2.other = d1
c = list()
print("d1 refcount:", sys.getrefcount(d1))
del a1
del a2
del b
del d1

print(sys.getrefcount(d2.other))
print(sys.getrefcount(d2))
print(sys.getrefcount(c))