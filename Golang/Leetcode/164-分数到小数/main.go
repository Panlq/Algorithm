package main

import (
	"fmt"
	"math"
)

func fractionToDecimal(numerator int, denominator int) string {
	if numerator == 0 {
		return "0"
	}
	var res []str // 定义存储字符的切片
	if (numerator * denominator) < 0 {
		append(res, "-")
	}
	numerator, denominator := math.Abs(numerator), math.Abs(denominator)
	a := numerator / denominator
	b := numerator % denominator
	append(res, string(a))
	// 判断小数
	if b == 0 {
		return string.Join(res, "")
	}

}

func main() {
	a := 8
	b := 2
	res := fractionToDecimal(a, b)
	fmt.Println("res: ", res)
}
