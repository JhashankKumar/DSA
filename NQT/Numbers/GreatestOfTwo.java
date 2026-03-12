package Numbers;

import java.util.Scanner;

public class GreatestOfTwo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();
        scanner.close();
        // int greatest = findGreatest(num1, num2);
        int greatest = findGreatestUsingMathMax(num1, num2);
        System.out.println("The greatest of " + num1 + " and " + num2 + " is: " + greatest);
    }

    private static int findGreatest(int a, int b) {
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }

    //using Math.max() method
    private static int findGreatestUsingMathMax(int a, int b) {
        return Math.max(a, b);
    }
}
