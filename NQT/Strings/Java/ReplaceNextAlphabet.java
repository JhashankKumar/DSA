import java.util.Scanner;

public class ReplaceNextAlphabet {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        String output = replaceWithNextAlphabet(input);
        String outputCaseSensitive = replaceWithNextAlphabetCaseSensitive(input);
        System.out.println("Original String: " + input);
        System.out.println("String after replacing with next alphabet: " + output);
        System.out.println("String after replacing with next alphabet (case-sensitive): " + outputCaseSensitive);
        scanner.close(); 
    }

    private static String replaceWithNextAlphabet(String input) {
        StringBuilder output = new StringBuilder();
        input = input.toLowerCase(); // Convert the string to lowercase for uniformity
        input = input.replaceAll("[^a-z]", ""); // Remove non-alphabetic characters and spaces

        for (char ch : input.toCharArray()) {
            if (ch == 'z') {
                output.append('a');
            } else {
                output.append((char) (ch + 1));
            }
        }

        return output.toString();
    }

    //mixed input of Capital and small letters give output in same case as input
    private static String replaceWithNextAlphabetCaseSensitive(String input) {
        StringBuilder output = new StringBuilder();

        for (char ch : input.toCharArray()) {
            if (Character.isLetter(ch)) {
                if (ch == 'z') {
                    output.append('a');
                } else if (ch == 'Z') {
                    output.append('A');
                } else {
                    output.append((char) (ch + 1));
                }
            } else {
                output.append(ch);
            }
        }

        return output.toString();
    }

}
