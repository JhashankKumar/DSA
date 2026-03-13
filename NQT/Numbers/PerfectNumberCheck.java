package Numbers;

import java.util.Scanner;

public class PerfectNumberCheck {
    // pefect number is a positive integer that is equal to the sum of its proper
    // divisors (excluding itself).
    public static void main(String[] args) {
        // input as string
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        String input = scanner.nextLine();
        int number = Integer.parseInt(input);
        if (isPerfectNumber(number)) {
            System.out.println(number + " is a perfect number.");
        } else {
            System.out.println(number + " is not a perfect number.");
        }
        scanner.close();
    }

    private static boolean isPerfectNumber(int number) {
        if (number <= 1) {
            return false; // Perfect numbers are greater than 1
        }
        int sum = 0;
        for (int i = 1; i <= number / 2; i++) {
            if (number % i == 0) {
                sum += i; // Add proper divisor to the sum
            }
        }
        return sum == number; // Check if the sum of divisors equals the original number
    }
}
