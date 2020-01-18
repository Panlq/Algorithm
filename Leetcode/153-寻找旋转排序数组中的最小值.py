"""
LeetCode 上第 153 号问题：寻找旋转排序数组中的最小值。也是《剑指Offer》上的一道经典题。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
例如，数组  [0，1，2，4，5，6，7] 可能变为 [4，5，6，7，0，1，2]
请找出其中最小的元素。假设数组中不存在重复元素
"""
from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    if nums[left] < nums[right]:
        return nums[0]
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 1, 2]
    print(findMin(arr))