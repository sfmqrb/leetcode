package main

import "fmt"

func main() {
	//fmt.Println(checkInclusion("wrlo", "helloworld"))
	fmt.Println(checkInclusion("a", "ab"))
}

func checkInclusion(s1 string, s2 string) bool {
	myHash := map[int32]int{}
	for _, val := range s1 {
		myHash[val]++
	}

	copiedHash := map[int32]int{}
	copyMap(myHash, copiedHash)
	var left int32 = 0
	for idx, val := range s2 {
		//fmt.Println("0 =>", idx, val)
		if _, ok := myHash[val]; ok {
			copiedHash[val]--
			//fmt.Println("1 =>", copiedHash)
		} else {
			copiedHash = map[int32]int{}
			copyMap(myHash, copiedHash)
			left = int32(idx + 1)
			continue
		}

		deleteIfZero(copiedHash, val)
		//fmt.Println(copiedHash)
		if len(copiedHash) == 0 {
			return true
		}

		for copiedHash[val] < 0 && left <= int32(idx) {
			//fmt.Println("left", left)
			copiedHash[int32(s2[left])]++
			left++
		}
		//fmt.Println("2 =>", copiedHash)
		deleteIfZero(copiedHash, val)
		//fmt.Println("3 =>", copiedHash)

	}
	return false
}

func deleteIfZero(copiedHash map[int32]int, val int32) {
	if copiedHash[val] == 0 {
		delete(copiedHash, val)
	}
}

func copyMap(myHash map[int32]int, copiedHash map[int32]int) {
	for key, val2 := range myHash {
		copiedHash[key] = val2
	}
}
