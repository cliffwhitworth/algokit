package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

// use memoization for fibRecursion (cache)
var memo = make(map[int]int)

func main() {
	// s := "Hello World!"
	// stringReversal(s)
	// charMapper(s)
	// arr := []int{1, 2, 3, 4, 5, 6, 7}
	// size := 2
	// arraySlicer(arr, size)
	// triangularN(5)
	// a1 := "Eleven plus two"
	// a2 := "Twelve plus one"
	// fmt.Printf("Strings are anagrams? %v\n", anagrams(a1) == anagrams(a2))
	// numSpirals(5)
	cli()
}

func stringReversal(s string) {
	// split and return reversed string
	arr := strings.Split(s, "")
	rs := make([]string, 0)
	for i := 0; i < len(arr); i++ {
		rs = append(rs, arr[len(arr)-i-1])
	}
	fmt.Println(strings.Join(rs, ""))
}

func charMapper(s string) {
	// split strings
	arr := strings.Split(s, "")
	charmap := make(map[string]int)

	// map characters
	for _, c := range arr {
		if _, ok := charmap[c]; ok {
			charmap[c]++
		} else {
			charmap[c] = 1
		}
	}

	// find the maxchar
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
	// strip spaces, lowercase, sort, return string
	re := regexp.MustCompile("\\s+")
	arr := strings.Split(re.ReplaceAllString(strings.ToLower(s), ""), "")
	sort.Strings(arr)
	return strings.Join(arr, "")
}

func triangularN(n int) {
	// interplay of i and j for loops, n(n+1) / 2
	o := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			// n(n+1) / 2
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

func numSpirals(n int) {
	// create an nxn array
	arr := make([][]int, n)
	for i := range arr {
		arr[i] = make([]int, n)
	}

	// initiate count, startRow, endRow, startCol, endCol
	c := 1
	sr := 0
	er := n - 1
	sc := 0
	ec := n - 1

	// fill the array with spiraling numbers
	// increment rows and cols to create spiral
	for sr <= er && sc <= ec {
		for i := sc; i < ec+1; i++ {
			arr[sr][i] = c
			c++
		}
		sr++

		for i := sr; i < er+1; i++ {
			arr[i][ec] = c
			c++
		}
		ec--

		for i := ec; i > sc-1; i-- {
			arr[er][i] = c
			c++
		}
		er--

		for i := er; i > sr-1; i-- {
			arr[i][sc] = c
			c++
		}
		sc++

	}

	// print in matrix form
	for i := range arr {
		fmt.Println(arr[i])
	}
}

func cli() {
	// Get user input
	fmt.Print("Enter an integer: ")
	reader := bufio.NewReader(os.Stdin)
	resp, err := reader.ReadString('\r')
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
	}
	n, err := strconv.Atoi(strings.Trim(resp, "\r"))
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
	}
	fmt.Printf("Fibonacci at %d is %d", n, fibRecursion(n))
}

func fibRecursion(n int) int {
	// check if cached
	if _, ok := memo[n]; ok {
		return memo[n]
	}

	if n < 2 {
		return n
	}

	result := fibRecursion(n-2) + fibRecursion(n-1)
	memo[n] = result

	return result
}
