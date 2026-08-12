package Numbers.Java;

import java.util.Scanner;

public class SumOfNNaturalNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive integer n to calculate the sum of the first n natural numbers: ");
        int number = scanner.nextInt();
        scanner.close();
        if (number < 1) {
            System.out.println("Please enter a positive integer.");
            return;
        }
        int sum = (number * (number + 1)) / 2; // Using the formula n(n+1)/2
        System.out.println("The sum of the first " + number + " natural numbers is: " + sum);
    }
}
