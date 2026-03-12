package Numbers;

public class Factorial {
    public static void main(String[] args) {
        int number = 5; // Example number
        long factorial = calculateFactorial(number);
        System.out.println("Factorial of " + number + " is: " + factorial);
    }

    private static long calculateFactorial(int number) {
        if (number == 0 || number == 1) {
            return 1;
        }
        long result = 1;
        for (int i = 2; i <= number; i++) {
            result *= i;
        }
        return result;
    }
}
