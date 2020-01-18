"""
LeetCode 上第 153 号问题：寻找旋转排序数组中的最小值。也是《剑指Offer》上的一道经典题。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
例如，数组  [0，1，2，4，5，6，7] 可能变为 [4，5，6，7，0，1，2]
请找出其中最小的元素
## 数组中存在重复元素
思路参考:https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/
"""
from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < nums[right]:
            # mid 有可能是最小值 或者在mid左边
            right = mid
        elif nums[mid] > nums[right]:
            # 最小值 在mid右边
            left = mid + 1
        else:
            # mid == right 去掉右边界 逐步逼近
            assert nums[mid] == nums[right]
            # right = right - 1
            right -= 1 # 此赋值方法比上面变量之间相减赋值多耗时8ms

    return nums[left]


if __name__ == "__main__":
    # arr = [3, 4, 5, 6, 1, 2]
    arr = [1, 1, 1, 1, 0, 1, 1]
    print(findMin(arr))