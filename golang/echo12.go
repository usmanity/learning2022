package main

// prints out each index and its value

import (
	"fmt"
	"os"
)

func main() {
	s, sep := "", ""
	for idx, arg := range os.Args[1:] {
		fmt.Println(idx, arg)
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}
