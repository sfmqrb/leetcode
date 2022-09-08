package main

import "fmt"

func main() {
	fmt.Println(characterReplacement("AAAA", 2))
}

func characterReplacement(s string, k int) int {
	myHash := map[byte]int{}
	left, right := 0, 0
	MAX := 0
	for left <= right && right < len(s) {
		myHash[s[right]]++
		if right-left+1-max(myHash) > k {
			myHash[s[left]]--
			left++
		}

		if right-left+1 > MAX {
			MAX = right - left + 1
		}
		right++
	}
	return MAX
}

func max(values map[byte]int) int {
	max := 0
	for _, val := range values {
		if val > max {
			max = val
		}
	}
	return max
}
