"""

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change

状态定义
状态转移方程
初始化+边界条件
画表格

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # 由于0无法用硬币组成，所以amount + 1
        # 初始化
        dp[0] = 0
        # f[1], f[2], f[3]...f[11]
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j-coin],  dp[j])
        
        return dp[amount] if dp[amount] != float('inf') else -1