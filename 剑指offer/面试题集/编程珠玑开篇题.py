"""
Q: 输入：一个最多包含n个正整数的文件，每个数都小于n，其中n=10^7(一千万)。如果在输入文件中有任何正数重复出现就是致命错误。没有其他数据与该正数相关联。
输出：按升序排列的输入正数的列表。


**约束：最多有1MB的内存空间可用，有充足的磁盘存储空间可用。运行时间最多几分钟，运行时间为10秒就不需要进一步优化。**
"""

MAX_SIZE = 10 ** 5

import time
import random
from bitarray import bitarray


class BitMap:
    def __init__(self, size):
        self.size = size
        self.array = bitarray(size)
        self.array.setall(0)

    def set(self, index):
        self.array[index] = 1
    
    def isTrue(self, index):
        return self.array[index] == 1


if __name__ == '__main__':
    arr = [i for i in range(MAX_SIZE)]
    random.shuffle(arr)

    ## 解决大数据排序
    bitmap = BitMap(MAX_SIZE)
    for i in arr:
        bitmap.set(i)

    for i in range(MAX_SIZE):
        if bitmap.isTrue(i):
            print(i)
            time.sleep(0.5)

    ## 在大数据中判断某个值是否存在
    print(bitmap.isTrue(64))


