package main

import (
	"fmt"
	"strings"
)

// 左旋数字数组切片
func rotateLeft(s []int, n int) []int{
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

//左旋字符串
func rotateLeftString(s string, n int) string{
	lens := len(s)
	arr := make([]string, lens)
	for k := range s {
		index := n + k
		if index >= lens {
			index -= lens
		}
		// fmt.Printf("%v(%c)\n", s[index], s[index])
		arr[k] = string(s[index])
	}

	return strings.Join(arr, "")
}


// func reverse(s string) string {
// 	r := []rune(s)
// 	for i, j := 0, len(r) - 1; i < j; i, j = i+1, j-1 {
// 		r[i], r[j] = r[j], r[i]
// 	}
// 	return string(r)
// }

// reverse 字符串
func reverse(s string, begin int, end int) string {
	r := []rune(s)
	for i, j := begin, end; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

// 左旋转字符串 剑指offer解法
func rotateLeftString2(s string, n int) string {
	length := len(s)
	result := s
	if (length < 0) {
		return s
	}

	if (0 <= n && n <= length) {
		pFBegin, pFEnd := 0, n - 1
		pSBegin, pSEnd := n, length - 1
		result = reverse(result, pFBegin, pFEnd)
		result = reverse(result, pSBegin, pSEnd)
		result = reverse(result, pFBegin, pSEnd)
	}
	return result
}

func main() {
	s := "abcfedg"
	// n := 2
	fmt.Println(reverse(s, 0, len(s) - 1))
	arrs := []int{5, 6, 7, 8, 9}
	res1 := rotateLeft(arrs, 2)
	fmt.Println(res1)
	res2 := rotateLeftString(s, 2)
	fmt.Println(res2)
	res3 :=  rotateLeftString2(s, 2)
	fmt.Println(res3)
	
}