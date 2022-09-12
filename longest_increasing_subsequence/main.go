package main

import "fmt"

func main() {
	a := []int{
		4, 2, 1, 4, 3, 4, 5, 8, 15,
	}
	k := 3
	fmt.Println(lengthOfLIS(a, k))
}

func lengthOfLIS(nums []int, k int) int {
	var dpArr []int
	max := 0
	l := len(nums)
	for i := 0; i < l; i++ {
		dpArr = append(dpArr, 0)
	}
	for idx, num := range nums {
	L:
		for idx2, count := range dpArr {
			if idx2 >= idx {
				break L
			}
			if Abs(nums[idx2]-num) <= k && nums[idx2] < num && dpArr[idx] < count+1 {
				dpArr[idx] = count + 1
				updateMax(&max, dpArr[idx])
			}
		}
		if 0 == dpArr[idx] {
			dpArr[idx] = 1
			updateMax(&max, 1)
		}

	}
	return max
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}


func updateMax(max *int, newVal int) {
	if newVal > *max {
		*max = newVal
	}
}