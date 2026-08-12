package Numbers.Java;

import java.util.Scanner;

public class HarshadNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();
        if (isHarshadNumber(number)) {
            System.out.println(number + " is a Harshad number.");
        } else {
            System.out.println(number + " is not a Harshad number.");   
        }
    }

    private static boolean isHarshadNumber(int num) {
        int sumOfDigits = 0;
        int temp = num;
        while (temp > 0) {
            sumOfDigits += temp % 10; // Add the last digit to the sum
            temp /= 10; // Remove the last digit
        }
        return num % sumOfDigits == 0; // Check if the number is divisible by the sum of its digits
    }
}
