package main

import "fmt"

/*
LeetCode 上第 153 号问题：寻找旋转排序数组中的最小值。也是《剑指Offer》上的一道经典题。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
例如，数组  [0，1，2，4，5，6，7] 可能变为 [4，5，6，7，0，1，2]
请找出其中最小的元素。
## 数组中存在重复元素
*/

/*
思路: 使用分而治之的方法, 注意到是有序旋转数组所以只有两种情况
1. s[mid] > s[right] 说明最小值在右边部分，left = mid + 1, 
2. s[mid] < s[right] 说明最小值在左边部分, right = mid
3. 如果有重复的元素, 即当 s[mid] == s[right] 时 只能采用逐步逼近方法 right-- 防止所有元素相同
*/

func findMin(nums []int) int{
	left, right := 0, len(nums) - 1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] > nums[right] {
			left = mid + 1
		} else if nums[mid] < nums[right] {
			right = mid
		} else {
			right--
		}
	}
	return nums[left]
}


func main() {
	// s := []int{4, 5, 6, 7, 0, 1, 2}
	s := []int{1, 1, 1, 1, 0, 1, 1}
	res := findMin(s)
	fmt.Printf("the min value is:%v\n", res)
}

