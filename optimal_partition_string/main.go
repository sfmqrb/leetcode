package main

import "fmt"

func main() {
	s := "abacaba"
	fmt.Println(partitionString(s))
}

func partitionString(s string) int {
	m := make(map[int32]int)
	count := 0
	for _, val := range s {
		m[val]++
		if m[val] == 2 {
			m = make(map[int32]int)
			count++
			m[val]++
		}
	}
	if len(m) > 0 {
		count++
	}
	return count
}