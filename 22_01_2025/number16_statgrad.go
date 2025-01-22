package main

import (
	"fmt"
	"math"
)

func main() {
	number16_statgrad()
}

func f(n int) int {
	if n == 0 {
		return n
	}

	if n%2 != 0 {
		return f(n-1) + 2*n - 1
	}

	return 4 * f(n/2)
}

func number16_statgrad() {
	var maxValue float64
	for i := 0; i < 1000; i++ {
		for j := 0; j < 1000; j++ {
			if f(i)-f(j) == 1045 {
				maxValue = math.Max(maxValue, float64(i-j))
			}
		}
	}

	fmt.Println(maxValue)
}
