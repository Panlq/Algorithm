"""
题目:
https://leetcode-cn.com/problems/valid-palindrome-ii/

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

输入: "aba"
输出: True

输入: "abca"
输出: True
解释: 你可以删除c字符。


字符串只包含从 a-z 的小写字母。字符串的最大长度是50000
"""

class Solution:
    def validPalindrome(self, s:str) ->bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j += 1
            return True
        
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high)or checkPalindrome(low, high - 1)
        
        return True

    def validPalindrome2(self, s:str) ->bool:
        isPalindrome = lambda s : s == s[::-1]
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return isPalindrome(s[low + 1: high]) or isPalindrome(s[low: high - 1])
        return True


if __name__ == '__main__':
    s = ['aba', 'abca', 'abda']
    so = Solution()
    for item in s:
        print(so.validPalindrome(item))
        print(so.validPalindrome2(item))