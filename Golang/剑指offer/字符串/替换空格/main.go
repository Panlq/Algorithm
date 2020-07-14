package main

import "fmt"
import "strings"

func main() {
	str := "We are happy"
	newStr := strings.ReplaceAll(str, " ", "%20")
	fmt.Printf("old: %s, ---> new: %s\n", str, newStr)
}