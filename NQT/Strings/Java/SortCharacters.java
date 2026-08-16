import java.util.*;
public class SortCharacters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        String outputAscending = sortCharactersInAscending(input);
        String outputDescending = sortCharactersInDescending(input);
        System.out.println("Original String: " + input);
        System.out.println("Sorted Characters String (Ascending): " + outputAscending);
        System.out.println("Sorted Characters String (Descending): " + outputDescending);
        scanner.close();
    }

    private static String sortCharactersInAscending(String string) {
        char[] characters = string.toCharArray();
        Arrays.sort(characters);
        return new String(characters);
    }

    private static String sortCharactersInDescending(String string) {
        char[] characters = string.toCharArray();
        Arrays.sort(characters);
        StringBuilder sortedString = new StringBuilder(new String(characters));
        return sortedString.reverse().toString();
    }
}
