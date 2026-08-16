public class RepeatedLettersInEachWord {
    // This program counts the number of repeated letters in each word of a given string.
    //if highest count is 1 then there are no repeated letters in that word
    //if two or more characters have the same highest count, it will return all the characters.

    public static void main(String[] args) {
        String input = "google is a search engine";
        countRepeatedLetters(input);
    }   

    private static void countRepeatedLetters(String input) {
        String[] words = input.split(" ");
        for (String word : words) {
            int[] count = new int[26];
            for (char ch : word.toCharArray()) {
                count[ch - 'a']++;
            }
            int maxCount = 0;
            for (int c : count) {
                if (c > maxCount) {
                    maxCount = c;
                }
            }
            System.out.print("Word: " + word + " - Repeated Letters: ");
            if (maxCount <= 1) {
                System.out.println("None");
            } else {
                for (int i = 0; i < count.length; i++) {
                    if (count[i] == maxCount) {
                        System.out.print((char) (i + 'a') + " ");
                    }
                }
                System.out.println();
            }
        }
    }
}
