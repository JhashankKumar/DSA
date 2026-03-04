import java.util.*;

public class CaptilizeFristAndLastCharOfWord {
    //for a given string, capitalize the first and last character of each word in the string.
    public static void main(String[] args) {
        String input = "hello world is java programming";
        String result = capitalizeFirstAndLastChar(input);
        System.out.println(result);
    }

    private static String capitalizeFirstAndLastChar(String input) {
        StringBuilder result = new StringBuilder();
        String[] words = input.split(" ");
        for (String word : words) {
            if (word.length() > 0) {
                char firstChar = Character.toUpperCase(word.charAt(0));
                char lastChar = Character.toUpperCase(word.charAt(word.length() - 1));
                String middlePart = word.substring(1, word.length() - 1);
                result.append(firstChar).append(middlePart).append(lastChar).append(" ");
            }
        }
        return result.toString().trim(); // Remove the trailing space
    }
}
