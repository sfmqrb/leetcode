package main

import (
	"fmt"
)

func main() {
	sArr := []string{
		"3", "2", "11",
		//"683339452288515879", "7846081062003424420", "4805719838",
		//"4840666580043", "83598933472122816064", "522940572025909479", "615832818268861533",
		//"65439878015", "499305616484085", "97704358112880133", "23861207501102", "919346676",
		//"60618091901581", "5914766072", "426842450882100996", "914353682223943129", "97",
		//"241413975523149135", "8594929955620533", "55257775478129", "528", "5110809",
		//"7930848872563942788", "758", "4", "38272299275037314530", "9567700", "28449892665",
		//"2846386557790827231", "53222591365177739", "703029", "3280920242869904137", "87236929298425799136",
		//"3103886291279",
	}
	k := 1

	fmt.Println(kthLargestNumber(sArr, k))

}

func kthLargestNumber(nums []string, k int) string {
	kMaxArr := make([]string, k, k)
	for _, strVar := range nums {
		idx := whereToLocate(kMaxArr, strVar)
		if idx == -1 {
			continue
		}
		shiftArr(kMaxArr, idx)
		kMaxArr[idx] = strVar
	}
	return kMaxArr[len(kMaxArr)-1]
}

func shiftArr(nums []string, after int) {
	i := len(nums) - 2
	for ; i >= after; i-- {
		nums[i+1] = nums[i]
	}
}

func whereToLocate(nums []string, num string) int {
	if cmp(num, nums[len(nums)-1]) == -1 || cmp(num, nums[len(nums)-1]) == 0 {
		return -1
	}
	i := 0
	for ; ; i++ {
		if cmp(nums[i], num) == -1 || cmp(nums[i], num) == 0 {
			return i
		}
	}
}

func cmp(str1 string, str2 string) int {
	if len(str1) < len(str2) {
		return -1
	} else if len(str1) > len(str2) {
		return 1
	} else if str1 < str2 {
		return -1
	} else if str1 > str2 {
		return 1
	}
	return 0
}
