"""
RGB排序，一个字符串，里面只有三种字符R G B，所有的R都在G的前面，
所有的G都在B的前面。将给定字符串按照此规律排序。要求不允许用辅助空间，
复杂度控制在O(N)。

假设源字符串:RGBBGRRBRGRBBG
参考: https://blog.csdn.net/jfkidear/article/details/50909129
在Python中字符串是不可变类型，所以还是要稍微借助一下list的
"""


def rgbSort(str):
    arrStr = list(str)
    i, j, k = 0, len(arrStr) - 1, 0
    while (k <= j):
        if arrStr[k] == 'R' and i != k:
            arrStr[i], arrStr[k] = arrStr[k], arrStr[i]
            i += 1
        elif arrStr[k] == 'B':
            arrStr[j], arrStr[k] = arrStr[k], arrStr[j]
            j -= 1
        else:
            k += 1
    return ''.join(arrStr)
        


if __name__ == '__main__':
    arrStr = 'RGBBGRRBRGRBBG'
    res = rgbSort('RGBBGRRBRRBBG')
    print('raw:', arrStr, 'sorted: ', res)