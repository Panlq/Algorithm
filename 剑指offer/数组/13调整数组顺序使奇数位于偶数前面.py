
"""

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，
偶数和偶数之间的相对位置不变
使用双向队列, 遍历数组， 奇数前插入，偶数后插入
"""

from collections import deque


def reOrderArray(array):
    odd = deque()
    l = len(array)
    for i in range(l):
        # 保证数组原有顺序, 结合奇数前插入，偶数后插入
        # 1先从后开始往前，先判断奇数
        if array[l-i-1] % 2 != 0:
            odd.appendleft(array[l-i-1])
        if array[i] % 2 == 0:
            odd.append(array[i])
    return list(odd)

if __name__ == '__main__':

    arr = [1, 2, 6, 3, 19, 25, 34, 12, 56, 74, 83, 19]
    print(reOrderArray(arr))