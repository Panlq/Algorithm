package main

import "fmt"


func solution(array []int) int {
	res, maxNum := 0, 0
	for _, num := range array {
		if maxNum < res {
			maxNum = res
		}
		if res >= 0 {
			res += num
		} else {
			res = num
		}
	}
	return maxNum
}

func main() {
	var array = []int{1, -2, 3, 10, -4, 7, 2, -5}
	res := solution(array)
	fmt.Printf("the max sum: %d", res)
}