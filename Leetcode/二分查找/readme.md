[【0x3f-灵神基础算法精讲 04】](https://www.bilibili.com/video/BV1AP41137w7/)

`[5, 7, 7, 8, 8, 10]`

返回非递减数组中第一个 ≥8 的数的位置，如果所有数都<8，返回数组长度

暴力做法：遍历每个数，询问是否 ≥8？ 时间复杂度 O(n)

# 二分查找的模型

红蓝染色法：约定如下

≥ target 表示在 target 右侧标记为蓝色

＜ target 表示在 target 左侧标记为红色

## 1. 左闭右闭

```golang
func lowerBound(nums []int, target int) int {
    left := 0
    right := len(nums) - 1
    // 闭区间[left, right]
    for left <= right {  // 区间不为空，继续轮询查询目标
        // right - left 防止溢出
        mid := left + (right - left) / 2
        /*
        循环不变量(即通过这次循环可以得知的具体不变的信息)
        nums[left] < target
        nums[right] >= target
        */
        if nums[mid] >= target {
            // 范围缩小到[left, mid-1]
            right = mid - 1
        } else {
            // 范围缩小到(mid+1, right)
            left = mid + 1
        }
    }

    // 此时 left 等于 right + 1
    // 因为 nums[left - 1] < target 且 nums[left] >= target，所以答案是 left  / right + 1
    return left
}

```

## 2. 左闭右开

```golang
func lowerBound(nums []int, target int) int {
    left := 0
    right := len(nums)
    // 左闭右开[left, right)
    for left < right {  // 区间不为空，继续轮询查询目标
        // right - left 防止溢出
        mid := left + (right - left) / 2
        /*
        循环不变量(即通过这次循环可以得知的具体不变的信息)
        nums[left] < target
        nums[right] >= target
        */
        if nums[mid] >= target {
            // 范围缩小到[left, mid)
            right = mid
        } else {
            // 范围缩小到(mid+1, right)
            left = mid + 1
        }
    }

    // 此时 left 等于 right
    // 因为 nums[left - 1] < target 且 nums[left] >= target，所以答案是 left  / right
    // 循环结束后 left == right
    return left
}

```

## 3. 左开右开

```golang

func lowerBound(nums []int, target int) int {
    left := -1
    right := len(nums)
    // 开区间 (left, right)
    for left + 1 < right {  // 区间不为空，继续轮询查询目标
        // right - left 防止溢出
        mid := left + (right - left) / 2
        /*
        循环不变量(即通过这次循环可以得知的具体不变的信息)
        nums[left] < target
        nums[right] >= target
        */
        if nums[mid] >= target {
            // 范围缩小到(left, mid)
            right = mid
        } else {
            // 范围缩小到(mid, right)
            left = mid
        }
    }

    // 此时 left 等于 right - 1
    // 因为 nums[right - 1] < target 且 nums[right] >= target，所以答案是 right
    return right
}

```

## 4. 总结

### 1. 左闭右闭

left=0, right=len(nums)-1

区间不为空的循环条件：left ≤ right

mid ≥ target: right = mid - 1

mid < target: left = mid + 1

### 2. 左闭右开

left = 0, right = len(nums)

区间不为空的循环条件: left < right

mid ≥ target: right = mid

mid < target: left = mid + 1

### 3. 左开右开

left = -1, right = len(nums)

区间不为空的循环条件：left + 1 < right

mid ≥ target: right = mid

mid < target: left = mid

# 举一反三

## 1. 获取第一个大于等于 target

ans = f(x)

## 2. 获取第一个大于 target

ans = f(x+1)

## 3. 获取最后一个小于 target

ans = f(x) - 1

## 4. 获取最后一个小于等于 target

ans = f(x+1)-1

```golang

func TestLowerBound(t *testing.T) {
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	target := 5
	// 找第一个大于等于 target 的下标  5

	fmt.Println(lowerBound(nums, target))

	// 找第一个大于 target 的下标  6

	fmt.Println(lowerBound(nums, target+1))

	// 找最后一个小于等于 target 的下标 5

	fmt.Println(lowerBound(nums, target+1) - 1)

	// 找最后一个小于 target 的下标  4

	fmt.Println(lowerBound(nums, target) - 1)
}
```

# 题目

以如下题目，来分析二分查找的多种模型(固定模式)

[34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-t9l9/)

给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target`，返回 `[-1, -1]`。

你必须设计并实现时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

<pre><strong>输入：</strong>nums = [5,7,7,8,8,10], target = 8
<strong>输出：</strong>[3,4]</pre>

**示例 2：**

<pre><strong>输入：</strong>nums = [5,7,7,8,8,10], target = 6
<strong>输出：</strong>[-1,-1]</pre>

**示例 3：**

<pre><strong>输入：</strong>nums = [], target = 0
<strong>输出：</strong>[-1,-1]</pre>

**提示：**

- `0 <= nums.length <= 10<sup>5</sup>`
- `-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>`
- `nums` 是一个非递减数组
- `-10<sup>9</sup> <= target <= 10<sup>9</sup>`
