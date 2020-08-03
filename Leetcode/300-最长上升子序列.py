
"""

给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

思路, 动态规划
dp[i]=max(dp[j])+1, 其中0≤j<i且num[j]<num[i]
最后，整个数组的最长上升子序列即所有 dp[i]dp[i] 中的最大值。

LIS length=max(dp[i]),其中0≤i<n

"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return  max(dp)

    
if __name__ == '__main__':
    a = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(a))