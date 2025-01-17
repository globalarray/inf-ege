package main

import (
	"fmt"
	"math"
	"os"
	"path/filepath"
)

func main() {
	//https://inf-ege.sdamgia.ru/problem?id=27694
	number24_reshuege()
	//result: 24
}

func number24_reshuege() {
	wd, err := os.Getwd()

	if err != nil {
		panic(err)
	}

	bytes, err := os.ReadFile(filepath.Join(wd, "assets", "18_01_2025", "zadanie24_1.txt"))

	if err != nil {
		panic(err)
	}

	var ml, temp int

	for idx, b := range bytes {
		if idx == 0 {
			if b == 'A' {
				temp++
			}
			continue
		}

		if (b == 'A' && bytes[idx-1] == 'B') || (b == 'B' && bytes[idx-1] == 'A') {
			temp++
			continue
		}

		ml = int(math.Max(float64(ml), float64(temp)))
		temp = 0
		continue
	}

	fmt.Println(ml)
}
