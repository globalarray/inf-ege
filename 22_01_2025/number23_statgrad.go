package main

import (
	"fmt"
)

func main() {
	number23_statgrad()
}

func f(x, y int) (result int) {
	if x < y || x == 10 || x == 15 {
		return 0
	}

	if x == y {
		return 1
	}

	if x%2 == 0 {
		result += f(x/2, y)
	}

	if x%3 == 0 {
		result += f(x/3, y)
	}

	return result + f(x-1, y)
}

func number23_statgrad() {
	fmt.Println(f(22, 1))
}
