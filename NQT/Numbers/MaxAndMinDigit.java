package Numbers;

public class MaxAndMinDigit {
    public static void main(String[] args) {
        int number = 12345; // Example number
        int maxDigit = findMaxDigit(number);
        int minDigit = findMinDigit(number);
        System.out.println("Maximum digit in " + number + " is: " + maxDigit);
        System.out.println("Minimum digit in " + number + " is: " + minDigit);
    }

    private static int findMaxDigit(int number) {
        int max = 0;
        while (number > 0) {
            int digit = number % 10;
            if (digit > max) {
                max = digit;
            }
            number /= 10;
        }
        return max;
    }

    private static int findMinDigit(int number) {
        int min = 9;
        while (number > 0) {
            int digit = number % 10;
            if (digit < min) {
                min = digit;
            }
            number /= 10;
        }
        return min;
    }
}
