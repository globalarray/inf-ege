package main

import (
	"fmt"
	"math/big"
)

func main() {
	//https://inf-ege.sdamgia.ru/problem?id=72574
	number16_reshuege()
	//result: 4090506
}

func f(n *big.Int) *big.Int {
	if n.Cmp(big.NewInt(3)) < 0 {
		return new(big.Int).Set(n)
	}
	nMinus1 := new(big.Int).Sub(n, big.NewInt(1))
	nMinus2 := new(big.Int).Sub(n, big.NewInt(2))

	result := new(big.Int).Mul(nMinus1, f(nMinus2))

	return result
}

func number16_reshuege() {
	sub := new(big.Int).Sub(f(big.NewInt(2025)), f(big.NewInt(2023)))

	fmt.Println(sub.Div(sub, f(big.NewInt(2021))))
}
