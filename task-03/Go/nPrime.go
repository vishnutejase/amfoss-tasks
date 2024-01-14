package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	if num < 2 {
		return false
	}
	for i := 2; float64(i) <= math.Sqrt(float64(num)); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func findPrimes(n int) []int {
	var primes []int
	for i := 2; i <= n; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes
}

func main() {
	var n int
	fmt.Print("Enter a number: ")
	fmt.Scanln(&n)
	result := findPrimes(n)
	fmt.Printf("Prime numbers up to %d are: %v\n", n, result)
}
