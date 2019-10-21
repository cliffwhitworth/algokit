package main

import (
	"fmt"
	"regexp"
	"sort"
	"strings"
)

func main() {
	// s := "Hello World!"
	// stringReversal(s)
	// charMapper(s)
	arr := []int{1, 2, 3, 4, 5, 6, 7}
	size := 2
	arraySlicer(arr, size)
	// triangularN(5)
	// a1 := "Eleven plus two"
	// a2 := "Twelve plus one"
	// fmt.Printf("Strings are anagrams? %v\n", anagrams(a1) == anagrams(a2))
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

func arraySlicer(arr []int, s int) {
	// t will be size of [][]int slices
	t := len(arr) / 2
	// is length of arr divided by s an integer?
	if len(arr)%s != 0 {
		// add 1 to t for extra slice
		t = int(len(arr)/2) + 1
	}

	slices := make([][]int, t)
	index := 0
	// fill the array of slices of size
	for i := 0; i < len(slices); i++ {
		if i < len(slices)-1 {
			slices[i] = arr[index : index+s]
			index += s
		} else {
			slices[i] = arr[index:]
		}
	}
	fmt.Println(slices)
}

func anagrams(s string) string {
	re := regexp.MustCompile("\\s+")
	arr := strings.Split(re.ReplaceAllString(strings.ToLower(s), ""), "")
	sort.Strings(arr)
	return strings.Join(arr, "")
}

func triangularN(n int) {
	o := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if j < i+1 {
				fmt.Print("O")
				o++
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
	fmt.Printf("Triangular number is %d", o)
}
