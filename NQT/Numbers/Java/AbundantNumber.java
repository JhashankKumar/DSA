package Numbers.Java;
import java.util.*;

public class AbundantNumber {
    // If the sum of divisors of a number is greater than the number then it is called abundant number.
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        if (isAbundant(number)) {
            System.out.println(number + " is an abundant number.");
        } else {
            System.out.println(number + " is not an abundant number.");
        }
        scanner.close();
    }

    // This method checks if a number is abundant by calculating the sum of its proper divisors and comparing it to the number itself.
    // in this method we checks from least abundant number which is 12 and we start sum of divisors from 1 because 1 is a proper divisor of all numbers.
    private static boolean isAbundant(int number) {
        if (number < 12) { // The smallest abundant number is 12
            return false;
        }
        int sumOfDivisors = 1; // Start with 1, which is a proper divisor
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                sumOfDivisors += i;
            }
        }
        return sumOfDivisors > number;
    }

    // This method calculates the sum of proper divisors of a number by iterating through possible divisors and summing those that divide the number evenly.
    private static int sumOfProperDivisors(int number) {
        int sum = 1; // Start with 1, which is a proper divisor
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                sum += i;
            }
        }
        return sum;
    }
}
