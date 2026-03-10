public class VowelsConsonantSpace {
    // Given a string, count the number of vowels and consonants and spaces in it.
    public static void main(String[] args) {
        String input = "Hello World";
        countVowelsAndConsonants(input);
    }

    private static void countVowelsAndConsonants(String input) {
        int vowelCount = 0;
        int consonantCount = 0;
        int spaceCount = 0;
        input = input.toLowerCase(); // Convert the input string to lowercase for easier comparison
        for (char ch : input.toCharArray()) {
            if (ch == ' ') {
                spaceCount++;
            } else if (isVowel(ch)) {
                vowelCount++;
            } else if (ch >= 'a' && ch <= 'z') {
                consonantCount++;
            }
        }
        System.out.println("Number of vowels: " + vowelCount);
        System.out.println("Number of consonants: " + consonantCount);
        System.out.println("Number of spaces: " + spaceCount);
    }

    private static boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
