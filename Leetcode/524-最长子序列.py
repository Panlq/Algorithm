"""
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，
该字符串可以通过删除给定字符串的某些字符来得到。
如果答案不止一个，返回长度最长且字典顺序最小的字符串。
如果答案不存在，则返回空字符串。

https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"


s = "abpcplea", d = ["a","b","c"]

输出: 
"a"

所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。

参考:https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/524-tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-dian-li-/
"""

from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestWord = ''
        for target in d:
            l1, l2 = len(longestWord), len(target)
            if (l1 > l2) or (l1 == l2 and longestWord < target):
                continue
            if self.isSubStr(s, target):
                longestWord = target
            
        return longestWord

    def isSubStr(self, s: str, target: str) -> bool:
        i, j = 0, 0
        while (i < len(s) and j < len(target)):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target)

    def findLongestWord2(self, s: str, d: List[str]) -> str:

        longestWord = ''
        rawStrLen = len(s)
        for target in d:
            targetLen = len(target)
            j = 0
            for i in range(rawStrLen):
                if j < targetLen and s[i] == target[j]:
                    j += 1
                if j == targetLen and (targetLen > len(longestWord) \
                    or (targetLen == len(longestWord) and target < longestWord)):
                    longestWord = target
                        
        return longestWord

    def findLongestWord3(self, s: str, d: List[str]) -> str:
        # 使用python内置方法，底层是C的支持，运行时间更快
        d.sort(key=lambda x: (-len(x), x)) # 对字典d进行排序，第一关键字是长度降序，第二关键字是字符串本身字典序
        def isSubStr(item):
            i = 0
            for j in item:
                k = s.find(j, i)  # 查找函数，后一个参数是查找起点
                if k == -1:
                    return False
                i = k + 1
            return True
        
        for item in d:
            if isSubStr(item):
                return item
        return ''
            


