public class ReverseString {
    public static void main(String[] args) {
        String input = "Hello World!";
        String output = reverseString(input);
        System.out.println("Original String: " + input);
        System.out.println("Reversed String: " + output);
    }

    private static String reverseString(String string) {
        StringBuilder reversed = new StringBuilder();
        for (int i = string.length() - 1; i >= 0; i--) {
            reversed.append(string.charAt(i));
        }
        return reversed.toString();
    }
}
