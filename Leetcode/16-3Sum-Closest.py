"""

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

https://leetcode-cn.com/problems/3sum-closest/solution/hua-jie-suan-fa-16-zui-jie-jin-de-san-shu-zhi-he-b/

"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        length = len(nums) - 1
        for i in nums:
            s, e = i + 1, length
            sum = nums[s] + nums[e] + nums[i]
            if abs(target-sum) < abs(target - ans):
                # 判断距离, 如果距离更小则替换
                ans = sum
            if sum > target:
                e -= 1
            elif sum < target:
                s += 1
            else:
                # 如果相等则直接返回
                return ans
        
        return ans
