package main

import "fmt"

func main() {
	arr1 := []int{2,3,4,54}
	arr2 := []int{4,12,14,51}
	fmt.Println(findMedianSortedArrays(arr1, arr2))
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	i,j := 0,0
	nn := make([]int, 0)
	for i < len(nums1) || j < len(nums2) {
		if i >= len(nums1) {
			nn = append(nn, nums2[j:]...)
			break
		} else if j >= len(nums2) {
			nn = append(nn, nums1[i:]...)
			break
		} else {
			if nums1[i] < nums2[j] {
				nn = append(nn, nums1[i])
				i++
			} else if nums1[i] >= nums2[j] {
				nn = append(nn, nums2[j])
				j++
			}
		}
	}

	size := len(nn)
	if size%2 == 0 {
		return (float64(nn[size/2]) + float64(nn[(size/2)-1]))/2.0
	} else {
		return float64(nn[size/2])
	}
}