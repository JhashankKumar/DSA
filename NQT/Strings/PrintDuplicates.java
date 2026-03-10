import java.util.*;
public class PrintDuplicates {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        printDuplicates(input);
        scanner.close();
    }

    private static void printDuplicates(String input) {
        // Implementation for printing duplicates
        input = input.toLowerCase(); // Convert the string to lowercase for uniformity
        input = input.replaceAll("[^a-z]", ""); // Remove non-alphabetic characters and spaces
        int[] freq = new int[26];
        // Count frequency of each character
        for (char ch : input.toCharArray()) {
            freq[ch - 'a']++;
        }
        // Print characters that appear more than once
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 1) {
                System.out.print((char) (i + 'a') + " ");
            }
        }
    }
}
