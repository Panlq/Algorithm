"""
Q:输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

思路：最简单的方法就是先排序，然后在遍历输出最小的K个数，方法简单粗暴。

另一种方法: 构建一个k个节点的最大堆，剩下的len - k 个元素依次跟堆顶元素比较如果比根节点小就替换，并重新调整最大堆，比他大就舍弃
"""


# 维护最大堆
LEFT = lambda i: 2 * i + 1
RIGHT = lambda i: 2 * i + 2


def max_heap_adjust(array, i, heap_size):
    while True:
        l, r = LEFT(i), RIGHT(i)
        largest = l if l < heap_size and array[l] > array[i] else i
        largest = r if r < heap_size and array[r] > array[largest] else largest
        if i == largest: break
        array[i], array[largest] = array[largest], array[i]
        i = largest


# 构建最大堆
def build_max_heap(array):
    heap_size = len(array)
    # 根据有子节点的数据量去构建堆
    for i in range(len(array) // 2 - 1, -1, -1):
        max_heap_adjust(array, i, heap_size)


def getLeastNums(array, k):
    res = []
    length = len(array)
    if length <= 0 or k <= 0 or k > length:
        return res
    res = array[:k]
    build_max_heap(res)
    for i in array[k:]:
        if i < res[0]:
            res[0] = i
            max_heap_adjust(res, 0, k)

    return res


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    result = getLeastNums(alist, 4)
    print(result)