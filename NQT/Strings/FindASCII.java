import java.util.*;

public class FindASCII {
    // Given a string, find the ASCII value of each character in the string.
    public static void main(String[] args) {
        String input = "Hello World";
        findASCIIValues(input);
    }

    private static void findASCIIValues(String input) {
        for (char ch : input.toCharArray()) {
            int asciiValue = (int) ch; // Get the ASCII value of the character
            System.out.println("Character: '" + ch + "' - ASCII Value: " + asciiValue);
        }
    }
}
