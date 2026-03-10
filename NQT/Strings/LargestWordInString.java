public class LargestWordInString {
    public static void main(String[] args) {
        String input = "The quick brown fox jumps over the lazy dog";
        String largestWord = findLargestWord(input);
        System.out.println("The largest word in the string is: " + largestWord);
    }

    private static String findLargestWord(String input) {
        String[] words = input.split(" ");
        String largestWord = "";

        for (String word : words) {
            if (word.length() > largestWord.length()) {
                largestWord = word;
            }
        }

        return largestWord;
    }
}
