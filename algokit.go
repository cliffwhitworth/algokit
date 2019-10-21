package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Hello World!"
	// stringReversal(s)
	charMapper(s)
}

func stringReversal(s string) {
	arr := strings.Split(s, "")
	rs := make([]string, 0)
	for i := 0; i < len(arr); i++ {
		rs = append(rs, arr[len(arr)-i-1])
	}
	fmt.Println(strings.Join(rs, ""))
}

func charMapper(s string) {
	arr := strings.Split(s, "")
	charmap := make(map[string]int)
	for _, c := range arr {
		if _, ok := charmap[c]; ok {
			charmap[c]++
		} else {
			charmap[c] = 1
		}
	}

	var maxchar string
	max := 0
	for k, v := range charmap {
		if v > max {
			maxchar = k
			max = v
		}
	}

	fmt.Printf("Maxchar = %s\n", maxchar)
}
