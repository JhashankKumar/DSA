public class RemovevVowels {
    public static void main(String[] args) {
        String input = "Hello World!";
        String output = removeVowels(input);
        System.out.println("Original String: " + input);
        System.out.println("String after removing vowels: " + output);  
    }

    private static String removeVowels(String string) {
        return string.replaceAll("[AEIOUaeiou]", "");
    }
}
 