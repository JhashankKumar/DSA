public class CheckAlphabets {
    public static void main(String[] args) {
        String input = "Hello World!";
        boolean result = checkAlphabets(input);
        if (result) {
            System.out.println("The string contains only alphabets.");
        } else {
            System.out.println("The string contains non-alphabet characters.");
        }
    }

    private static boolean checkAlphabets(String string) {
        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            if (!Character.isLetter(ch)) {
                return false; // Return false if a non-alphabet character is found
            }
        }
        return true; // Return true if all characters are alphabets
    }

    // Alternative method using regular expressions
    private static boolean checkAlphabetsUsingRegex(String string) {
        return string.matches("[a-zA-Z]+"); // Returns true if the string contains only alphabets
    }

    // this method prints non existing characters in the string
    private static void printNonAlphabets(String string) {
        System.out.println("Non-alphabet characters in the string:");
        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            if (!Character.isLetter(ch)) {
                System.out.print(ch + " "); // Print non-alphabet characters
            }
        }
        System.out.println(); // New line after printing all non-alphabet characters
    }
}
