package main

import "math/rand"

const xrand = 16

func StatRandomNumbers(n int) (int, int) {
	var a, b int

	for i := 0; i < n; i++ {
		if rand.Intn(xrand) < xrand/2 {
			a++
		} else {
			b++
		}
	}
	return a, b
}

func main() {
	var num int = 100
	x, y := StatRandomNumbers(num)

	print("Result: ", x, " + ", y, " = ", num, "? ")
	println(x+y == num)
}
