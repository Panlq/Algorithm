"""
Q: 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置。
S: 建立一个哈希表, 第一次扫描的时候，统计每个字符的出现次数，第二次扫描的时候，如果该字符出现的次数为1，
则返回这个字符的位置

python3.7使用 dict是默认有序的，所以可以第二部可以直接扫描字典，可以省区扫描原字符串可以节省时间
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""

class Solution:
    def __init__(self):
        pass

    def firstNotRepeatingChar(self, ss):
        length = len(ss)
        if length == 0:
            return -1
        data = dict()
        for i in range(length):
            if ss[i] not in data:
                data[ss[i]] = 1
            else:
                data[ss[i]] += 1
        
        for i in range(length):
            if data[ss[i]] == 1:
                return i
        return -1
    