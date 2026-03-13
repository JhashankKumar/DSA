package Numbers;

public class SumOfDigits {
    public static void main(String[] args) {
        int number = 12345; // You can change this value to test with different numbers
        int sum = calculateSumOfDigits(number);
        System.out.println("The sum of the digits in " + number + " is: " + sum);
    }

    private static int calculateSumOfDigits(int number) {
        int sum = 0;
        while (number != 0) {
            sum += number % 10; // Add the last digit to the sum
            number /= 10; // Remove the last digit
        }
        return sum;
    }
}
