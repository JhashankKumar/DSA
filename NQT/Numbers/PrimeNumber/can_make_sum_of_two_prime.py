# find given number can be expressed as sum of two prime numbers or not and print those two prime numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def can_make_sum_of_two_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return True, i, n - i
    return False, None, None

def main():
    n = int(input("Enter a number: "))
    can_make_sum, prime1, prime2 = can_make_sum_of_two_primes(n)
    if can_make_sum:
        print(f"{n} can be expressed as the sum of two prime numbers: {prime1} + {prime2}")
    else:
        print(f"{n} cannot be expressed as the sum of two prime numbers.")

if __name__ == "__main__":
    main()