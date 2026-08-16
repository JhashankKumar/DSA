package Strings.Java;

public class ChangeCaseOfCharacters {
    // Given a string, change the case of each character in the string.
    public static void main(String[] args) {
        String input = "Hello World";
        String result = changeCase(input);
        System.out.println("Original String: " + input);
        System.out.println("String with changed case: " + result);
    }

    private static String changeCase(String input) {
        StringBuilder result = new StringBuilder();
        for (char ch : input.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                result.append(Character.toLowerCase(ch)); // Change to lowercase
            } else if (Character.isLowerCase(ch)) {
                result.append(Character.toUpperCase(ch)); // Change to uppercase
            } else {
                result.append(ch); // Non-alphabetic characters remain unchanged
            }
        }
        return result.toString();
    }
}