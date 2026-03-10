import java.util.*;
public class ValidAnagram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the first string:");
        String str1 = scanner.nextLine();
        System.out.println("Enter the second string:");
        String str2 = scanner.nextLine();
        scanner.close();
        boolean isAnagram = areAnagramsUsingArray(str1, str2);
        if (isAnagram) {
            System.out.println("The strings are anagrams.");
        } else {
            System.out.println("The strings are not anagrams.");
        }
    }

    private static boolean areAnagramsUsingArray(String str1, String str2) {
        // Remove spaces and convert to lowercase
        str1 = str1.replaceAll("\\s", "").toLowerCase();
        str2 = str2.replaceAll("\\s", "").toLowerCase();
        // If lengths are different, they cannot be anagrams
        if (str1.length() != str2.length()) {
            return false;
        }
        // Convert strings to character arrays and sort them
        char[] charArray1 = str1.toCharArray();
        char[] charArray2 = str2.toCharArray();
        Arrays.sort(charArray1);
        Arrays.sort(charArray2);
        // Check if sorted character arrays are equal
        return Arrays.equals(charArray1, charArray2);
    }

    private static boolean areAnagramsUsingHashMap(String str1, String str2) {
        // Remove spaces and convert to lowercase
        str1 = str1.replaceAll("\\s", "").toLowerCase();
        str2 = str2.replaceAll("\\s", "").toLowerCase();
        // If lengths are different, they cannot be anagrams
        if (str1.length() != str2.length()) {
            return false;
        }
        // Create a frequency map for characters in the first string
        Map<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : str1.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        // Decrease the frequency based on characters in the second string
        for (char c : str2.toCharArray()) {
            if (!frequencyMap.containsKey(c) || frequencyMap.get(c) == 0) {
                return false; // Character not found or frequency mismatch
            }
            frequencyMap.put(c, frequencyMap.get(c) - 1);
        }
        return true; // All characters matched
    }
}
