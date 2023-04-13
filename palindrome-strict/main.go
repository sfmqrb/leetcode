package main

func isStrictlyPalindromic(n int) bool {
	if n < 0 {
		return false
	}
	for i := 2; i < n - 1; i++ {
		newVal := 0
		n2 := n
		for n2 != 0 {
			newVal *= i
			newVal += n2 % i
			n2 /= i
		}
		if newVal != n {
			return false
		}
	}
	return true
}
