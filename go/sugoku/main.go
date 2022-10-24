package main

import (
	"fmt"
)

func main() {
	var board [10][10]int

	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			board[i][j] = (i * 10) + j
		}
	}

	fmt.Print(board[4][2])
}
