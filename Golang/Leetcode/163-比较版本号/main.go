package main

import "fmt"

// If (a > b ? a : b).(type)
func If(condition bool, trueVal, falseVal interface{}) interface{} {
	if condition {
		return trueVal
	}
	return falseVal
}

func compareVersion(version1 string, version2 string) int {
	p1, p2 := 0, 0
	len1, len2 := len(version1), len(version2)
	end := If(len1 > len2, len1, len2).(int)
	for p1 < end || p2 < end {
		var v1, v2 int
		for p1 < len1 && version1[p1] != '.' {
			v1 = v1*10 + int(version1[p1]-'0')
			p1++
		}

		for p2 < len2 && version2[p2] != '.' {
			v2 = v2*10 + int(version2[p2]-'0')
			p2++
		}

		if v1 > v2 {
			return 1
		} else if v1 < v2 {
			return -1
		}

		p1++
		p2++
	}
	return 0
}

func main() {
	a := "7.02.13"
	b := "7.002.0012"

	res := compareVersion(a, b)
	fmt.Println("the res is :", res)

}
