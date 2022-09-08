package main

import "fmt"

func main() {
	fmt.Println(characterReplacement("AAAA", 2))
}

func characterReplacement(s string, k int) int {
	var max, left, right int
	charCount := map[byte]int{}

	sum := 1
	charCount[s[0]] = 1

	sLen := len(s)
	L: for {
		c := checkCharCountState(k, charCount, sum)
		fmt.Println(left, right, c)
		switch c {
		case -1:
			removeByteToMap(s[left], charCount, &sum)
			left++
		case 1:
			right++
			if right >= sLen {
				break L
			}
			addByteToMap(s[right], charCount, &sum)
		case 0:
			toBeNewMax := right - left + 1
			right++
			if toBeNewMax > max {
				max = toBeNewMax
			}
			if right >= sLen {
				break L
			}
			addByteToMap(s[right], charCount, &sum)
		}
	}
	if max == 0 {
		return len(s)
	}
	return max
}

func addByteToMap(b byte, charCount map[byte]int, sum *int) {
	charCount[b]++
	*sum++
}

func removeByteToMap(b byte, charCount map[byte]int, sum *int) {
	charCount[b]--
	*sum--
	if charCount[b] == 0 {
		delete(charCount, b)
	}
}

func findMaxChar(charCount map[byte]int) (byte, int) {
	var maxVal int
	var maxKey byte
	for key, val := range charCount {
		if val > maxVal {
			maxKey = key
			maxVal = val
		}
	}
	return maxKey, maxVal
}

func checkCharCountState(k int, charCount map[byte]int, sum int) int {
	_, maxVal := findMaxChar(charCount)
	//fmt.Println("=>", k, maxVal, sum)
	if sum > k+maxVal {
		// left out
		return -1
	} else if sum < k+maxVal {
		// right in
		return 1
	}
	// right in
	return 0
}
