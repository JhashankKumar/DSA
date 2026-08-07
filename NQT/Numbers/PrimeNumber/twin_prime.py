# find the twin prime numbers in the given range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num) and is_prime(num + 2):
            print(f"({num}, {num + 2})")

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print(f"Twin prime numbers between {start} and {end} are:")
    twin_primes_in_range(start, end)

if __name__ == "__main__":
    main()