"""
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers

输入: version1 = "0.1", version2 = "1.1"
输出: -1


输入: version1 = "1.0.1", version2 = "1"
输出: 1
"""



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        n1, n2 = len(ver1), len(ver2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(ver1[i]) if i < n1 else 0
            i2 = int(ver2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal 
        return 0

     
class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        len1, len2 = len(version1), len(version2)
        end = max(len1, len2)
        while (p1 < end or p2 < end):
            v1, v2 = 0, 0
            while (p1 < len1 and version1[p1] != '.'):
                v1 = v1 * 10 + ord(version1[p1]) - 48   # '0' Asiico = 48
                p1 += 1
            
            while (p2 < len2 and version2[p2] != '.'):
                v2 = v2 * 10 + ord(version2[p2]) - 48
                p2 += 1

            if v1 != v2:
                return 1 if v1 > v2 else -1
        
            p1 += 1
            p2 += 1

        return 0



if __name__ == '__main__':
    s = Solution()
    s2 = Solution2()
    a = '7.02.01'
    b = '7.2.003'
    print(s.compareVersion(a, b))
    print(s2.compareVersion(a, b))
