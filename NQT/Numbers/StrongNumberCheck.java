package Numbers;

public class StrongNumberCheck {
    //strong number is a number whose sum of the factorial of digits is equal to the original number.
    public static void main(String[] args) {
        int number = 145; // You can change this value to test with different numbers
        boolean isStrong = isStrongNumber(number);
        if (isStrong) {
            System.out.println(number + " is a Strong Number.");
        } else {
            System.out.println(number + " is not a Strong Number.");
        }
    }

    private static boolean isStrongNumber(int number) {
        int originalNumber = number;
        int sumOfFactorials = 0;

        while (number > 0) {
            int digit = number % 10;
            sumOfFactorials += factorial(digit);
            number /= 10;
        }

        return sumOfFactorials == originalNumber;
    }

    private static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
}
