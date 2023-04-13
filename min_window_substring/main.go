package main

import "fmt"

func main() {
	s := "helloworld"
	t := "ell"

	fmt.Println(minWindow(s, t))
}

func minWindow(s string, t string) string {
	counterMap := make(map[byte]int)
	remaining := len(t)
	for i := range t {
		counterMap[t[i]]++
	}
	if len(t) > len(s) {
		return ""
	}
	left, right := 0, 0
	retLeft, retRight := 0, len(s)
	for right < len(s) {
		if v, ok := counterMap[s[right]]; ok {
			if v > 0 {
				remaining--
			}
			counterMap[s[right]]--
		}
		for remaining <= 0 {
			if retRight-retLeft >= right-left {
				retLeft, retRight = left, right
			}
			if _, ok := counterMap[s[left]]; ok {
				counterMap[s[left]]++
				if counterMap[s[left]] > 0 {
					remaining++
				}
			}
			left++
		}
		right++
	}

	if retRight == len(s) && retLeft == 0 {
		return ""
	}
	return s[retLeft : retRight+1]
}
