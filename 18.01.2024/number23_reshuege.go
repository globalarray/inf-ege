package main

import (
	"fmt"
)

func main() {
	//https://inf-ege.sdamgia.ru/problem?id=9206
	number23_reshuege()
	//result: 39
}

func f(x, y int) int {
	if x > y {
		return 0
	}

	if x == y {
		return 1
	}

	return f(x+1, y) + f(x+3, y) + f(x+(x-1), y)
}

func number23_reshuege() {
	fmt.Println(f(2, 10))
}
