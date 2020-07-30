"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，
空间复杂度是O(1)。
leetcode137
"""

class Solution:
    def FindNumsAppearOnce(self, array):
        length = len(array)
        if length <= 0:
            return []

        resultExclusiveOR = 0
        for i in array:
            resultExclusiveOR ^= i
        firstBitIs = self.FindFirstBit(resultExclusiveOR)
        num1, num2 = 0, 0
        for i in array:
            if self.BitIs(i, firstBitIs):
                num1 ^= i
            else:
                num2 ^= i 
        return num1, num2

    def FindFirstBit(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit <= 32:
            indexBit += 1
            num = num >> 1
        return indexBit
    
    def BitIs(self, num, indexBit):
        num = num >> indexBit
        return num & 1


    
class Solution2:
    def FindNumsAppearOnce(self, nums):
        length = len(nums)
        if length <= 0:
            return []

        diff = 0
        for i in nums:
            diff ^= i
    
        n1, n2 = 0, 0
        minDiff = self.getMinDiff(diff)
        for num in nums:
            if minDiff & num == 0:
                n1 ^= num
        n2 = diff ^ n1
        return n1, n2

    def getMinDiff(self, num):
        # 保留一个低位是1的数字
        # 取负号其实就是先取反，再加 1，需要 补码 的知识。最后再和原数相与就会保留最低位的 1。比如 1010，先取反是 0101，再加 1，就是 0110，再和 1010 相与，就是 0010 了
        return num & (-num)


    
if __name__ == '__main__':

    a = [1,2,3,5,3,2,1,6,7,8,7,6,5,4]

    print(Solution2().FindNumsAppearOnce(a))