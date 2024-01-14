use std::io;

fn is_prime(num: u32) -> bool {
    if num < 2 {
        return false;
    }
    for i in 2..=((num as f64).sqrt() as u32) {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn find_primes(n: u32) -> Vec<u32> {
    let mut primes = Vec::new();
    for i in 2..=n {
        if is_prime(i) {
            primes.push(i);
        }
    }
    primes
}

fn main() {
    println!("Enter a number: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: u32 = input.trim().parse().expect("Please enter a valid number");

    let result = find_primes(n);
    println!("Prime numbers up to {} are: {:?}", n, result);
}
