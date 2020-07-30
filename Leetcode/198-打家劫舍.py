"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber

1. 原本想法，奇偶数分别求和，求最大值，没考虑到[2, 1, 1, 2]这种情况
2. 动态规划:
定义状态：
    设动态规划列表dp, dp[i]代表前i个房子在满足条件下能获得的最高金额
转移方程：
    设，有n个房子,前n间能偷窃到的最高金额是dp[n], 前n-1间能偷窃到的最高金额是dp[n-1], 
    此时向这些房子后加一间房，此房间价值为num
    加一间房子后：由于不能抢相邻的房子，意味着抢第n+1 间就不能抢第n间，那么前n+1间房能偷窃到的
    最高金额dp[n+1]就是以下两种情况
        1. 不抢n+1， dp[n+1]=dp[n]
        2. 抢n+1, 此时不能抢n ==> dp[n+1] = dp[n-1] + num[n]

    细心的我们发现： 难道在前 nn 间的最高金额 dp[n]dp[n] 情况下，第 nn 间一定被偷了吗？假设没有被偷，那 n+1n+1 间的最大值应该也可能是 dp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 吧？其实这种假设的情况可以被省略，这是因为：

    假设第 nn 间没有被偷，那么此时 dp[n] = dp[n-1]dp[n]=dp[n−1] ，此时 dp[n+1] = dp[n] + num = dp[n-1] + numdp[n+1]=dp[n]+num=dp[n−1]+num ，即两种情况可以 合并为一种情况 考虑；
    假设第 nn 间被偷，那么此时 dp[n+1] = dp[n] + numdp[n+1]=dp[n]+num 不可取 ，因为偷了第 nn 间就不能偷第 n+1n+1 间。
    最终的转移方程： dp[n+1] = max(dp[n],dp[n-1]+num)dp[n+1]=max(dp[n],dp[n−1]+num)

    作者：jyd
    链接：https://leetcode-cn.com/problems/house-robber/solution/da-jia-jie-she-dong-tai-gui-hua-jie-gou-hua-si-lu-/


"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sumOdd = 0
        sumEven = 0

        for i, v in enumerate(nums):
            if i % 2 == 0:
                sumEven += v
                sumEven = max(sumEven, sumOdd)

            else:
                sumOdd += v
                sumOdd = max(sumOdd, sumEven)
        return max(sumOdd, sumEven)


# 动态规划
class Solution2:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur



    
if __name__ == '__main__':
    a = [2,1,1,2]
    s = Solution()
    print(s.rob(a))