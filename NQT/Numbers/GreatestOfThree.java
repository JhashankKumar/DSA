package Numbers;

import java.util.Scanner;

public class GreatestOfThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();
        System.out.print("Enter the third number: ");
        int num3 = scanner.nextInt();
        scanner.close();
        // int greatest = findGreatest(num1, num2, num3);
        int greatest = findGreatestUsingMathMax(num1, num2, num3);
        System.out.println("The greatest of " + num1 + ", " + num2 + ", and " + num3 + " is: " + greatest);
        
    }

    private static int findGreatest(int a, int b, int c) {
        if (a >= b && a >= c) {
            return a;
        } else if (b >= a && b >= c) {
            return b;
        } else {
            return c;
        }
    }

    //using Math.max() method
    private static int findGreatestUsingMathMax(int a, int b, int c) {
        return Math.max(a, Math.max(b, c)); 
    }
}
