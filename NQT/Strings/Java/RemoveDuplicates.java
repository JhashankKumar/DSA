import java.util.Scanner;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        String output = removeDuplicates(input);
        System.out.println("String after removing duplicates: " + output);
        scanner.close();
    }

    private static String removeDuplicates(String input) {
        input = input.toLowerCase(); // Convert the string to lowercase for uniformity
        input = input.replaceAll("[^a-z]", ""); // Remove non-alphabetic characters and spaces
        StringBuilder result = new StringBuilder();
        boolean[] seen = new boolean[26]; // To track seen characters

        for (char ch : input.toCharArray()) {
            if (!seen[ch - 'a']) { // If the character has not been seen before
                seen[ch - 'a'] = true; // Mark the character as seen
                result.append(ch); // Append the character to the result
            }
        }
        return result.toString();
    }
}
