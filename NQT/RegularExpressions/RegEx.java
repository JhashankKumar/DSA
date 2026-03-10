package RegularExpressions;

import java.util.*;

public class RegEx {
    public static void main(String[] args) {
        System.out.println("Regular Expressions in Java:");
        System.out.println("1. Remove Spaces");
        System.out.println(RemoveSpaces());
        System.out.println("2. Remove Digits");
        System.out.println(RemoveDigits());
        System.out.println("3. Keep Only Alphabets");
        System.out.println(KeepOnlyAlphabets());
        System.out.println("4. Remove Special Characters");
        System.out.println(RemoveSpecialCharacters());
        System.out.println("5. Remove Multiple Spaces");
        System.out.println(RemoveMultipleSpaces());
        System.out.println("6. Count Digits");
        System.out.println(CountDigits());
        System.out.println("7. Validate Email");
        System.out.println(ValidateEmail());
        System.out.println("8. Validate Phone Number");
        System.out.println(ValidatePhoneNumber());
        System.out.println("9. Remove Vowels");
        System.out.println(RemoveVowels());
        System.out.println("10. Remove Consonants");
        System.out.println(RemoveConsonants());
         
    }

    //remove spaces from the input string using regular expressions
    // + denotes one or more occurrences of the preceding element, which in this case is \\s (whitespace character)
    private static String RemoveSpaces() { 
        String input = "  Hello   World!  ";
        String output = input.replaceAll("\\s+", "");
        System.out.println("String after removing spaces: '" + output + "'");
        return output;
    }   

    //remove Digits from the input string using regular expressions
    private static String RemoveDigits() {
        String input="Java123Programming456";
        String output = input.replaceAll("\\d+", "");
        System.out.println("String after removing digits: '" + output + "'");
        return output;
    }

    //keep only alphabets from the input string using regular expressions
    private static String KeepOnlyAlphabets() {
        String input = "Hello123World456";
        String output = input.replaceAll("[^a-zA-Z]", "");
        System.out.println("String after keeping only alphabets: '" + output + "'");
        return output;
    }

    //remove special characters from the input string using regular expressions
    private static String RemoveSpecialCharacters() {
        String input = "Hello@#World$%^&*(2026)+|?";
        String output = input.replaceAll("[^a-zA-Z0-9]", "");
        System.out.println("String after removing special characters: '" + output + "'");
        return output;
    }
    
    //remove multiple spaces from the input string using regular expressions
    private static String RemoveMultipleSpaces() {
        String input = "This   is   a   string   with   multiple   spaces.";
        String output = input.replaceAll("\\s+", " ");
        System.out.println("String after removing multiple spaces: '" + output + "'");
        return output;
    }

    //count the number of digits in the input string using regular expressions
    private static int CountDigits() {
        String input = "Hello123World456";
        // int count = input.replaceAll("\\D", "").length();/
        int count = input.replace("[^0-9]", "").length();
        System.out.println("Number of digits in the string: " + count);
        return count;
    }

    private static boolean ValidateEmail() {
        String email = ""; // Example email address to validate
        String emailRegex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        return email.matches(emailRegex);
    }

    //validate phone number using regular expressions
    private static boolean ValidatePhoneNumber() {
        String phoneNumber = ""; // Example phone number to validate
        // String phoneRegex = "^\\d{10}$"; // Example regex for 10-digit phone number/
        String phoneRegex = "[0-9]{10}"; // Example regex for 10-digit phone number
        return phoneNumber.matches(phoneRegex);
    }

    //Remove Vowels from the input string using regular expressions
    private static String RemoveVowels() {
        String input = "Hello World!";
        String output = input.replaceAll("[AEIOUaeiou]", "");
        System.out.println("String after removing vowels: '" + output + "'");
        return output;
    }

    //Remove Consonants from the input string using regular expressions
    private static String RemoveConsonants() {
        String input = "Hello World!";
        String output = input.replaceAll("[^aeiouAEIOU]", "");
        System.out.println("String after removing consonants: '" + output + "'");
        return output;
    }

    //Split String by Multiple Delimiters using regular expressions
    private static String[] SplitStringByMultipleDelimiters() {
        String input = "Hello, World! This is a test.";
        String[] output = input.split("[,!.\\s]+");
        System.out.println("String after splitting by multiple delimiters: " + Arrays.toString(output));
        return output;
    }


}
