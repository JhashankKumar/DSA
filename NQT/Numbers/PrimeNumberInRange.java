package Numbers;

public class PrimeNumberInRange {
    public static void main(String[] args) {
        int lowerBound = 10; // You can change this value to set the lower bound of the range
        int upperBound = 50; // You can change this value to set the upper bound of the range

        System.out.println("Prime numbers between " + lowerBound + " and " + upperBound + ":");
        for (int number = lowerBound; number <= upperBound; number++) {
            if (isPrime(number)) {
                System.out.print(number + " ");
            }
        }
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
}
