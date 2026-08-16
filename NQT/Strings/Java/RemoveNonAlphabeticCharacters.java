public class RemoveNonAlphabeticCharacters {
    //remove all occurrences of non-alphabetic characters from a string

    public static void main(String[] args) {
        String input = "H3ll0 W0rld! @2024";
        String output = removeNonAlphabeticCharacters(input);
        System.out.println("Original String: " + input);
        System.out.println("String after removing non-alphabetic characters: " + output);
    }
    public static String removeNonAlphabeticCharacters(String string) {
        StringBuilder result = new StringBuilder();
        for (char ch : string.toCharArray()) {
            if (Character.isLetter(ch)) {
                result.append(ch);
            }
        }
        return result.toString();
    }
}
