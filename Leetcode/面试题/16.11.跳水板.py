"""
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diving-board-lcci

输入：
shorter = 1
longer = 2
k = 3
输出： [3,4,5,6]
解释：
可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。

设longer 使用i个, 则shorter = k - i
f(i) = shorter*(k-i) + longer * i
     = shorter * k + (longer - shorter) * i

"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [0] * (k +  1)
        for i in range(k + 1):
            res[i] = shorter * (k - i) + longer * i
        return res