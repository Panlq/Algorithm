"""
LeetCode上第 191 号问题：编写一个函数，输入是一个无符号整数，
返回其二进制表达式中数字位数为  ‘1’  的个数。
"""

class Solution:
    def hammingWeight(self, n):
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res

    def hammingWeight2(self, n):
        res = 0
        while n != 0:
            res += (n & 1)
            n = n >> 1
        return res