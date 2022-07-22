package main

import (
	"fmt"
	"os"
	"strings"
)

// 1.1 join all including arg[0]

func main() {
	fmt.Println(strings.Join(os.Args[0:], "\n"))
}
