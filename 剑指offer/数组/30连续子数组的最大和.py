"""
Q:HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,
到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)

S: 连续累加的子数组和，如果大于零则继续累加，否则就重新放弃原有的求和，从下一个数开始重新求和计算

解题思路，动态规划
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian-shi-ti-42-lian-xu-zi-shu-zu-de-zui-da-he-do-2/
"""


def solution(nums):
    res, maxNum = 0, nums[0]
    for num in nums:
        res = res + num if res >= 0 else num
        if res > maxNum:
            maxNum = res
    return maxNum


def solutions(nums):
    for i in range(1, len(nums)):
        nums[i] += max(nums[i-1], 0)
    return max(nums)


if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print(solution(arr))