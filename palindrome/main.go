func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	x2 := x
	val := 0
	for (x != 0) {
		val *= 10
		val += x % 10
		x /= 10
	}

	return x2 == val
}
