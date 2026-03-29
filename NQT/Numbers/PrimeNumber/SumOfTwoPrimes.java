package Numbers.PrimeNumber;

public class SumOfTwoPrimes {
    public static void main(String[] args) {
        int number = 28; // You can change this value to test with different numbers

        if (canBeExpressedAsSumOfTwoPrimes(number)) {
            System.out.println(number + " can be expressed as the sum of two prime numbers.");
        } else {
            System.out.println(number + " cannot be expressed as the sum of two prime numbers.");
        }
    }

    private static boolean canBeExpressedAsSumOfTwoPrimes(int n) {
        if (n < 2) {
            return false; // The smallest sum of two primes is 2 (1 + 1)
        }
        for (int i = 2; i <= n / 2; i++) {
            if (isPrime(i) && isPrime(n - i)) {
                return true; // Found two prime numbers that sum up to n
            }
        }
        return false; // No such pair found
    }

    private static boolean isPrime(int number) {
        if (number <= 1) {
            return false; // Prime numbers are greater than 1
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // If divisible by any number other than 1 and itself, it's not prime
            }
        }
        return true; // If no divisors found, it's a prime number
    }

    //prints all the pairs of prime numbers that sum up to the given number
    public static void printPrimePairs(int n) {
        System.out.println("Pairs of prime numbers that sum up to " + n + ":");
        for (int i = 2; i <= n / 2; i++) {
            if (isPrime(i) && isPrime(n - i)) {
                System.out.println(i + " + " + (n - i) + " = " + n);
            }
        }
    }
}
