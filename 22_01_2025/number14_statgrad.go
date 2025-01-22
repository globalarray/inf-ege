package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	number14_statgrad()
}

func convert(x string, base int) (r int) {
	letters := map[rune]int{
		'A': 10,
		'B': 11,
		'C': 12,
		'D': 13,
		'E': 14,
		'F': 15,
	}

	for i := 0; i < len(x); i++ {
		if v, ok := letters[rune(x[i])]; ok {
			r += v * int(math.Pow(float64(base), float64(len(x)-(i+1))))
			continue
		}

		n, err := strconv.Atoi(string(x[i]))

		if err != nil {
			panic(err)
		}

		r += n * int(math.Pow(float64(base), float64(len(x)-(i+1))))
	}

	return r
}

func number14_statgrad() {
	for i := 16; i < 100; i++ {
		if (convert("AB967D8", i)+convert("E435A98", i))%(i-1) == 0 {
			fmt.Println(i)
		}
	}
}
