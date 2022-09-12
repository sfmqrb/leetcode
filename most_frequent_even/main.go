package main

import "fmt"

func main() {
	a := make([]int, 10, 10)
	b := append(a, 10, 10, 1, 12)
	fmt.Println(mostFrequentEven(b))
}

func mostFrequentEven(nums[]int) int {
	evenCount := make(map[int]int)
	//
	maxVal := -1
	maxCount := 0

	for _, val := range nums {
		if val % 2 != 0 {
			continue
		}
		evenCount[val/2] += 1
		if evenCount[val/2] > maxCount {
			maxCount = evenCount[val/2]
			maxVal = val
		} else if evenCount[val/2] == maxCount {
			if maxVal > val {
				maxVal = val
			}
		}
	}

	if maxCount == 0 {
		return -1
	}

	return maxVal
}