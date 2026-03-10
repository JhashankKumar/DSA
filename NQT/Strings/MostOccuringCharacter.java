public class MostOccuringCharacter {
    public static void main(String[] args) {
        String input = "Hello World";
        char mostOccurringChar = findMostOccurringCharacter(input);
        System.out.println("The most occurring character in the string is: '" + mostOccurringChar + "'");
    }

    private static char findMostOccurringCharacter(String input) {
        int[] freq = new int[26]; 
        input = input.toLowerCase(); // Convert the string to lowercase for uniformity
        input = input.replaceAll("[^a-z]", ""); // Remove non-alphabetic characters and spaces
        
        // Count frequency of each character
        for (char ch : input.toCharArray()) {
            freq[ch - 'a']++;
        }

        // Find the character with the maximum frequency
        char mostOccurringChar = ' ';
        int maxFreq = 0;

        for (int i = 0; i < freq.length; i++) {
            if (freq[i] > maxFreq) {
                maxFreq = freq[i];
                mostOccurringChar = (char) (i + 'a');
            }
        }

        return mostOccurringChar;
    }
    
}
