/*
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
- 假定n级台阶的跳法看成 n的函数即 f(n)
		n=1, 1		// 当n=1时, 只有一种跳法
f(n) =  n=2, 2		// 当n=2时, 有两种跳法
		n>2, f(n-1) + f(n-2)
		// 当n>2时, 第一次跳的时候就有两种跳法
		- 1.第一次只跳1级, 此时跳法数目等于后面剩下的n-1级台阶的跳法的数目 即 f(n-1)
		- 2.第一次跳2级, 此时跳法数目等于后面剩下的n-2级台阶的跳法的数目 即f(n-2)
*/

/*
举一反三: 如果一个人上台阶可以一次上1个,2个，3个则函数就不一样了
		1,  					  n=1
		2,  					  n=2
f(n) =  4, 						  n=3
		f(n-1) + f(n-2) + f(n-3)  n>3
动态规划中的三个重要的概念: 最优子结构, 边界, 状态转移公式
*/

package main

import (
	"fmt"
	"time"
)

// 时间复杂度 o(2^n)
func getClinbingWays(n int) int {
	if n < 1 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	} else {
		return getClinbingWays(n-1) + getClinbingWays(n-2)
	}
}

// 使用备忘录算法计算 o(n) 空间复杂度 o(n)
func getClinbingWaysWithHashMap(n int, hashmap map[int]int) int {
	if n < 1 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	}

	if _, ok := hashmap[n]; ok {
		return hashmap[n]
	}

	temp := getClinbingWaysWithHashMap(n-1, hashmap) + getClinbingWaysWithHashMap(n-2, hashmap)
	hashmap[n] = temp
	return temp
}



// 分析递归中有很多重复的计算过程，所以可以从后往前推, 一步步利用之前计算的结果递推
// 只需要保留前两个的结果即可计算下一个

// 递推法 时间复杂度o(n) 空间复杂度o(1)
func getClinbingWaysOp(n int) int {
	if n < 1 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	}

	temp, a, b := 0, 1, 2
	for i := 3; i <= n; i++ {
		temp = a + b
		a = b
		b = temp
	}

	return temp
}


func main() {
	// var res int
	start := time.Now()
	fmt.Printf("getClinbingWays-->%d\n", getClinbingWays(50))
	tc := time.Since(start)
	fmt.Printf("getClinbingWays time cost = %v\n", tc)
	
	// start2 := time.Now()
	// hm := make(map[int]int)
	// res = getClinbingWaysWithHashMap(50, hm)
	// fmt.Printf("getClinbingWaysWithHashMap-->:%v\n", res)
	// tc2 := time.Since(start2)
	// fmt.Printf("getClinbingWays time cost = %v\n", tc2)

	// start3 := time.Now()
	// res = getClinbingWaysOp(50)
	// fmt.Printf("getClinbingWaysOp-->:%v\n", res)
	// tc3 := time.Since(start3)
	// fmt.Printf("getClinbingWaysOp time cost = %v\n", tc3)
}
