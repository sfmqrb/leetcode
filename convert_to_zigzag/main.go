package main

import (
	"fmt"
	"strings"
)
func main() {
	s, numRows := "sajjad", 2
	fmt.Println(convert(s, numRows))
}


func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	if numRows == 0 {
		return ""
	}

	stringBuilders := make([]*strings.Builder, numRows)
	nextStep := true
	j := 0
	for i, c := range s {
		if i < numRows {
			stringBuilder := &strings.Builder{}
			stringBuilders[i] = stringBuilder
		}

		(stringBuilders[j]).WriteRune(c)

		if (nextStep && j == numRows-1) || ((!nextStep) && j == 0) {
			nextStep = !nextStep
		}

		if nextStep {
			j++
		} else {
			j--
		}
	}

	var ans strings.Builder
	for _, stringBuilder := range stringBuilders {
		if stringBuilder != nil {
			ans.WriteString(stringBuilder.String())
		}
	}

	return ans.String()
}
