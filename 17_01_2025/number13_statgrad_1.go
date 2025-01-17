package main

import "fmt"

func main() {
  //https://imgur.com/a/XkEjJ3Z
	number23_statgrad()
  //result: 21
}

func f(x, lim int, s string) int {
	if x > lim || x == 12 {
		return 0
	}

	if x == lim {
		return 1
	}

	return f(x+1, lim, s+"+") + f(x*2, lim, s+"*") + f(x*x, lim, s+"^")
}

func number23_statgrad() {
	fmt.Println(f(3, 25, ""))
}
