"""
Q:在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数 

S: 根据已知条件缩小查找范围
1. 首先选取数组右上角的数字，如果该数字等于要查找的数字，查找过程结束
2. 如果右上角数字大于要查找的数字，剔除这个数字所在的列
3. 如果小于要查找的数字，剔除这个选取数字所在的行。

S2: numpy isin

1  2  8  9
2  4  9  12
4  7  10  13
6  8  11 15


"""

import numpy as np

def contain(arr, target):
    newarr = np.asarray(arr)
    return np.isin(target, newarr)

def find(array, target):
    rows = len(array)
    cols = len(array[0])
    if rows > 0 and cols > 0:
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if target == array[row][col]:
                return True
            elif target < array[row][col]:
                col -= 1
            else:
                row += 1
        return False

if __name__ == '__main__':
    arr = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]

    print(contain(arr, 13))
    print(find(arr, 10))