def is_prime(num)
  return false if num < 2
  (2..Math.sqrt(num)).each do |i|
    return false if num % i == 0
  end
  true
end

def find_primes(n)
  primes = []
  (2..n).each do |i|
    primes << i if is_prime(i)
  end
  primes
end

puts "Enter a number: "
n = gets.chomp.to_i
result = find_primes(n)
puts "Prime numbers up to #{n} are: #{result}"
