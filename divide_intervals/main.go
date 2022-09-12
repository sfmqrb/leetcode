package main

import (
	"fmt"
	"sort"
)

type iint [][]int



func main() {
	a := iint {
		{441459,446342},
		{801308,840640},
		{871890,963447},
		{228525,336985},
		{807945,946787},
		{479815,507766},
		{693292,944029},
		{751962,821744},
	}

	fmt.Println(minGroups(a))
}
func (c iint) Len() int      { return len(c) }
func (c iint) Swap(i, j int) { c[i], c[j] = c[j], c[i] }
func (c iint) Less(i, j int) bool { return c[i][0] < c[j][0] }


func minGroups(intervals [][]int) int {
	count := 0
	intervals2 := iint(intervals)
	sort.Sort(intervals2)
	//fmt.Println(intervals2)

	var grArr []int

	for _, arr := range intervals {
		//fmt.Println(arr)
		//fmt.Println("grArr", grArr)
		added := false
		L: for idx, gr := range grArr {
			//fmt.Println("H")
			if gr < arr[0] {
				grArr[idx] = arr[1]
				added = true
				break L
			}
		}
		if !added {
			grArr = append(grArr, arr[1])
			count++
		}
	}

	return count
}