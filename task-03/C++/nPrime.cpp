#include <iostream>
#include <vector>
#include <cmath>

bool isPrime(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

std::vector<int> findPrimes(int n) {
    std::vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            primes.push_back(i);
        }
    }
    return primes;
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::vector<int> result = findPrimes(n);
    std::cout << "Prime numbers up to " << n << " are: ";
    for (int prime : result) {
        std::cout << prime << " ";
    }
    std::cout << std::endl;
    return 0;
}
