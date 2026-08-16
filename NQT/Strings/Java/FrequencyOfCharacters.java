import java.util.Scanner;

public class FrequencyOfCharacters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        frequencyOfCharacters(input);
        scanner.close();
    }

    public static void frequencyOfCharacters(String str) {
        str = str.toLowerCase(); // Convert the string to lowercase for uniformity
        str = str.replaceAll("[^a-z]", ""); // Remove non-alphabetic characters and spaces
        int[] freq = new int[26]; 

        // Count frequency of each character
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i); 
            freq[ch - 'a']++;
        }

        // Print the frequency of each character
        System.out.println("Character Frequency:");
        for (int i = 0; i < freq.length; i++) {
            if (freq[i] > 0) {
                System.out.println((char) (i + 'a') + ": " + freq[i]);
            }
        }
    }
}
