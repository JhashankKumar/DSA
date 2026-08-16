public class FindNonExistibngAlphabets {
    public static void main(String[] args) {
        String input = "hello world";
        findNonExistingAlphabets(input);
    }

    private static void findNonExistingAlphabets(String input) {
        boolean[] alphabetExists = new boolean[26]; // To track existing alphabets
        input = input.toLowerCase(); // Convert to lowercase for uniformity

        // Mark the existing alphabets in the input string
        for (char ch : input.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') {
                alphabetExists[ch - 'a'] = true; // Mark the alphabet as existing
            }
        }

        System.out.println("Alphabets that do not exist in the input string:");
        for (int i = 0; i < 26; i++) {
            if (!alphabetExists[i]) {
                char missingAlphabet = (char) (i + 'a'); // Convert index back to character
                System.out.print(missingAlphabet + " ");
            }
        }
    }
}
