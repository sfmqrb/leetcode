package main

import (
	"fmt"
)

func reverse(x int) int {
	val := 0
	for (x != 0) {
		// fmt.Println(x, x % 10)
		val *= 10 
		val += x % 10
		x /= 10
	}

	if (1<<31 < val) || (-1<<31 > val) {
		return 0
	}

	return val
}

func main() {
	x := -123
	fmt.Println(reverse(x))
}
