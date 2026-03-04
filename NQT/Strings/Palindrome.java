import java.util.*;
public class Palindrome {
    // Given a string, check if it is a palindrome or not.
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string:");
        String input = scanner.nextLine();
        scanner.close();
        if (isPalindrome(input)) {
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }
    }

    private static boolean isPalindrome(String input) {
        String cleanedInput = input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase(); // Remove non-alphanumeric characters and convert to lowercase
        String reversedInput = new StringBuilder(cleanedInput).reverse().toString(); // Reverse the cleaned input
        return cleanedInput.equals(reversedInput); // Check if the cleaned input is equal to its reverse
    }
}
