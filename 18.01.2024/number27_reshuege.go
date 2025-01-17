package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"path/filepath"
	"slices"
	"strconv"
	"strings"
)

func main() {
	//https://inf-ege.sdamgia.ru/problem?id=28129
	number27_reshuege()
	//result: 728 977
  //        9982 9992
}

func number27_reshuege() {
	wd, err := os.Getwd()

	if err != nil {
		panic(err)
	}

	pth := path.Join(wd, "assets", "18_01_2025")

	ab, err := readFile(filepath.Join(pth, "28129_A.txt"))

	if err != nil {
		panic(err)
	}

	bb, err := readFile(filepath.Join(pth, "28129_B.txt"))

	if err != nil {
		panic(err)
	}

	f := func(ab []int) []int {
		numbers := make([]int, 2)

		for xid, x := range ab[1:] {
			for yid, y := range ab[1:] {
				if xid == yid {
					continue
				}
				if x%160 != y%160 {
					if x%7 == 0 || y%7 == 0 {
						if numbers[0]+numbers[1] < x+y {
							numbers = []int{x, y}
						}
					}
				}
			}
		}
		return numbers
	}

	for _, arr := range [][]int{ab, bb} {
		nums := f(arr)
		slices.Sort(nums)

		fmt.Printf("%d %d\n", nums[0], nums[1])
	}
}

func readFile(filename string) (s []int, err error) {
	f, err := os.Open(filename)

	defer func() { _ = f.Close() }()

	if err != nil {
		return s, err
	}

	reader := bufio.NewReader(f)

	for {
		if str, err := reader.ReadString('\n'); err == nil {
			n, err := strconv.Atoi(strings.TrimSpace(str))

			if err != nil {
				return s, err
			}

			s = append(s, n)
			continue
		}
		break
	}

	return s, nil
}
