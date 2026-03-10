public class MostRepeatedCharacter {
    public static void main(String[] args) {
        String input = "hello world";
        char mostRepeatedChar = findMostRepeatedCharacter(input);
        System.out.println("Most repeated character: " + mostRepeatedChar);
    }

    private static char findMostRepeatedCharacter(String input) {
        int[] count = new int[26];
        char mostRepeatedChar = ' ';
        int maxCount = 0;

        for (char ch : input.toCharArray()) {
            count[ch - 'a']++;
            if (count[ch - 'a'] > maxCount) {
                maxCount = count[ch - 'a'];
                mostRepeatedChar = ch;
            }
        }

        return mostRepeatedChar;
    }
}
