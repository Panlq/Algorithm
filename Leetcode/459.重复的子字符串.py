
"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。
输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。


1. 如果一个字符串可以由多个重复子串构成，即具有循环节 设最小循环节用a来表示，
他代表通过子串a重复多次可以构成s 即s换成a来表示就是aa···aaa，由多少个最小循环节a构成s，
那么就有几个a
2. 找循环节一个一个对比比较麻烦，最简单方法就是s+s就可以直接增加多一倍的循环节
3. 假设原来s=aaaa，那ss=s+s=aaaa aaaa 因为是不断重复的循环节，可以通过简单的屏蔽的第一个字符，
然后再在ss中寻找s 因为屏蔽第一个字符，即第一个最小循环节被破坏，所以找到的s应该是从第二个循环节开始
4. 但倘若不是由一个子串重复构成 即s=abcd，那ss=abcd abcd=s+s 屏蔽掉第一个字符，又因不匹配，
所以在ss中寻找s，一定是对应着新增s的位置，即s.size()处

https://leetcode-cn.com/problems/repeated-substring-pattern/
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).find(s, 1) != len(s)