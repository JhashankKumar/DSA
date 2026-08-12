package Numbers.Java;

public class PalindromeNumbersInRange {
    public static void main(String[] args) {
        int start = 10; // Example start of range
        int end = 100; // Example end of range
        System.out.println("Palindrome numbers between " + start + " and " + end + ":");
        for (int i = start; i <= end; i++) {
            // if (isPalindrome(i)) {
            //     System.out.print(i + " ");
            // }
            if (isPalindromeString(i)) {
                System.out.print(i + " ");
            }
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
        // String str = Integer.toString(number);
        String str = String.valueOf(number);
        String reversedStr = new StringBuilder(str).reverse().toString();
        return str.equals(reversedStr);
    }
}
