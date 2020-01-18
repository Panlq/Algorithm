package main

import "fmt"

/*
LeetCode 上第 153 号问题：寻找旋转排序数组中的最小值。也是《剑指Offer》上的一道经典题。
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
例如，数组  [0，1，2，4，5，6，7] 可能变为 [4，5，6，7，0，1，2]
请找出其中最小的元素。假设数组中不存在重复元素
*/


// 简单粗暴的方法, 直接遍历 时间复杂度O(N), 空间复杂度O(1)
func findMin(s []int) {
	var minValue int = s[0]
	for _, v := range s[1:] {
		if minValue > v {
			minValue = v
		}
	}
	fmt.Printf("the min value is:%v\n", minValue)
}

/*
优化思路: 使用分而治之的方法, 注意到是有序旋转数组所以只有两种情况
1. s[mid] > s[right] 说明最小值在右边部分，left = mid + 1, 
2. s[mid] < s[right] 说明最小值在左边部分, right = mid
*/

func findMinOp(nums []int) int{
	left, right := 0, len(nums) - 1
	if nums[left] < nums[right] {
		return nums[left]  // 无旋转
	}
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}


func main() {
	s := []int{4, 5, 6, 7, 0, 1, 2}
	findMin(s)
	res := findMinOp(s)
	fmt.Printf("the min value is:%v\n", res)
}

func remove(slice []int, i int) []int {
	copy(slice[i:], slice[i+1:])
	// return a new slice not the raw
	return slice[:len(slice)-1]
}

func reverse(s []int) {
	// reverses a slice of int in place
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

// 旋转切片 返回新的数组
// 新数组下表为原数组下标+偏移量, 如果超出最大长度则从左边开始
func rotate(s []int, n int) []int {
	lens := len(s)
	arr := make([]int, lens)
	for k := range s {
		index := n + k
		if index >= lens {
			index -= lens
		}
		arr[k] = s[index]
	}
	return arr
}
