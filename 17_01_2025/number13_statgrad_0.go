package main

import "fmt"

func main() {
  //https://imgur.com/a/NMwWrWU
	number23_statgrad()
  //result: 53
}

func f(x, lim int) int {
	if x < lim || x == 10 || x == 15 {
		return 0
	}

	if x == lim {
		return 1
	}

	r := f(x-1, lim)

	if x%2 == 0 {
		r += f(x/2, lim)
	}

	if x%3 == 0 {
		r += f(x/3, lim)
	}

	return r
}

func number23_statgrad() {
	fmt.Println(f(22, 1))
}
