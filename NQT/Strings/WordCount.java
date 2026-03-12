public class WordCount {
    public static void main(String[] args) {
        String input = "Hello world! This is a test string.";
        int wordCount = countWords(input);
        System.out.println("Number of words in the string: " + wordCount);
    }

    private static int countWords(String input) {
        if (input == null || input.trim().isEmpty()) {
            return 0; // Return 0 for null or empty strings
        }
        String[] words = input.trim().split("\\s+"); // Split by whitespace
        return words.length;
    }
}
