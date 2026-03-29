package Numbers.PrimeNumber;

import java.util.Scanner;

public class TwinPrime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the lower bound of the range: ");
        int lowerBound = scanner.nextInt();
        System.out.print("Enter the upper bound of the range: ");
        int upperBound = scanner.nextInt();
        System.out.println("Twin prime pairs between " + lowerBound + " and " + upperBound + ":");
        for (int number = lowerBound; number <= upperBound - 2; number++) {
            if (isPrime(number) && isPrime(number + 2)) {
                System.out.println("(" + number + ", " + (number + 2) + ")");
            }
        }
        scanner.close();
    }

    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false; // Prime numbers are greater than 1
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false; // If divisible by any number other than 1 and itself, it's not prime
            }
        }
        return true; // If no divisors found, it's a prime number
    }
}
