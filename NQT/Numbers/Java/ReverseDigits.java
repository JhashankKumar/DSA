package Numbers.Java;

public class ReverseDigits {
    public static void main(String[] args) {
        int number = 12345; // You can change this value to test with different numbers
        int reversedNumber = reverseDigits(number);
        System.out.println("Original number: " + number);
        System.out.println("Reversed number: " + reversedNumber);
    }

    private static int reverseDigits(int number) {
        int reversed = 0;
        while (number != 0) {
            reversed = reversed * 10 + number % 10;
            number /= 10;
        }
        return reversed;
    }

    // Alternative method using String manipulation
    private static int reverseDigitsUsingString(int number) {
        String numberStr = String.valueOf(number);
        String reversedStr = new StringBuilder(numberStr).reverse().toString();
        return Integer.parseInt(reversedStr);
    }
}
