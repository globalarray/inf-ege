package main

import (
	"fmt"
	"math"
)

func main() {
	//https://inf-ege.sdamgia.ru/problem?id=27620
	number17_reshuege()
	//result: 7313889
}

func number17_reshuege() {
	var c, mn int

	for i := 10837; i < 13920; i++ {
		if i%17 == 0 {
			nums := []int{7, 15, 18, 34}

			var suit bool

			for _, n := range nums {
				if i%n == 0 {
					suit = true
					break
				}
			}

			if suit {
				continue
			}

			c++
			mn = int(math.Max(float64(mn), float64(i)))
		}
	}

	fmt.Printf("%d%d", c, mn)
}
