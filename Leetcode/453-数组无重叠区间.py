"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals

"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> (int, List[List[int]]):
        intervals.sort(key=lambda x : x[-1])
        
        count = 1 # 第一个区间不相交
        cur_end = intervals[0][1]
        res = [intervals[0]]
        for item in intervals:
            if item[0] >= cur_end:
                # 找到一个选择区间
                count += 1
                cur_end = item[1]
                res.append(item)
        return count, res


if __name__ == '__main__':
    a = [[1,2], [2,3], [3,4], [1,3]]
    c, res = Solution().eraseOverlapIntervals(a)
    print(c)
    print(res)