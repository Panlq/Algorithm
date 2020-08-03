

"""
标签：数组遍历
首先对数组进行排序，排序后固定一个数 nums[i]nums[i]，再使用左右指针指向 nums[i]nums[i]后面的两端，数字分别为 nums[L]nums[L] 和 nums[R]nums[R]，计算三个数的和 sumsum 判断是否满足为 00，满足则添加进结果集
如果 nums[i]nums[i]大于 00，则三数之和必然无法等于 00，结束循环
如果 nums[i]nums[i] == nums[i-1]nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
当 sumsum == 00 时，nums[L]nums[L] == nums[L+1]nums[L+1] 则会导致结果重复，应该跳过，L++L++
当 sumsum == 00 时，nums[R]nums[R] == nums[R-1]nums[R−1] 则会导致结果重复，应该跳过，R--R−−
时间复杂度：O(n^2)O(n^2)，nn 为数组长度

作者：guanpengchn
链接：https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        length = len(nums)
        if length < 3:
            return res
        # 排序inplace  O(nlogn)
        nums.sort()
        # 找Base + 双指针
        for i in range(nums):
            if nums[i] > 0:
                break  # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 去重
            left = i + 1
            right = length - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i] + nums[left] + nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right += 1
                    left += 1
                    right += 1
                elif sum < 0:
                    # 由于已经排序所以往右靠增大sum
                    left += 1
                elif sum > 0:
                    # 往小了靠
                    right -= 1
                else:
                    pass

        return res

