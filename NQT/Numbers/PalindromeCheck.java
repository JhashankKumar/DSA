package Numbers;

public class PalindromeCheck {
    public static void main(String[] args) {
        int number = 12321; // Example number
        if (isPalindrome(number)) {
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
        // Using string method
        if (isPalindromeString(number)) {
            System.out.println(number + " is a palindrome (using string method).");
        } else {
            System.out.println(number + " is not a palindrome (using string method).");
        }
    }

    private static boolean isPalindrome(int number) {
        int originalNumber = number;
        int reversedNumber = 0;

        while (number > 0) {
            int digit = number % 10;
            reversedNumber = reversedNumber * 10 + digit;
            number /= 10;
        }

        return originalNumber == reversedNumber;
    }

    //using string
    private static boolean isPalindromeString(int number) {
        String str = Integer.toString(number);
        String reversedStr = new StringBuilder(str).reverse().toString();
        return str.equals(reversedStr); 
    }
}
