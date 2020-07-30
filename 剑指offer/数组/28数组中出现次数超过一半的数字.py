"""
Q：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。

由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。


"""

def solutionOne(arr):
    """
    基于Parition函数的O(n)算法
    """
    pass


def parition(data, length, start, end):
    pass


# 思路
"""
采用数字相互抵消的思想, 在遍历数组时存储两个值
一个当前遍历的数值result 初始值为nubers[0]
一个该数字的标记times, 初始值为1
当下一个数字与result相等时, times += 1, 否则 times -= 1
当times的值变为0时, 则将下一个数字的值赋值给result, 并将times置为1， 

如果数组中存在出现次数超过数组长度一半的数， 最后一次将times置为1的数就是答案
算法最后重新遍历一遍数组，验证结果

时间复杂度O(N)
"""
def moreThanHalfNum(numbers):
    result = numbers[0]
    times = 1
    for i in range(1, len(numbers)):
        if times == 0:
            result = numbers[i]
            times = 1
        elif result == numbers[i]:
            times += 1
        else:
            times -= 1
    times = 0
    # 验证找到的数字是否出现了一半多
    for i in range(len(numbers)):
        if numbers[i] == result:
            times += 1
    return result if times > len(numbers) // 2 else 0


def moreThanHalfNum2(numbers):
    from collections import Counter
    if not numbers: return 0
    count = Counter(numbers).most_common()
    if count[0][1] > len(numbers) // 2:
        return count[0][0]
    return 0

if __name__ == '__main__':
    arr = [1,2,3,2,2,2,5,4,2]
    print(moreThanHalfNum2(arr))