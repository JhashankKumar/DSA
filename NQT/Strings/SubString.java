public class SubString {
    //check if a string is a substring of another string
    public static void main(String[] args) {
        String mainString = "Hello World!";
        String subString = "World";
        boolean isSubstring = isSubstring(mainString, subString);
        System.out.println("Main String: " + mainString);
        System.out.println("Sub String: " + subString);
        System.out.println("Is Substring: " + isSubstring);
        int index = indexOfSubstring(mainString, subString);
        System.out.println("Index of Substring: " + index);
    }

    private static boolean isSubstring(String mainString, String subString) {
        return mainString.contains(subString);
    }

    //find the index of the first occurrence of a substring in a string
    private static int indexOfSubstring(String mainString, String subString) {
        return mainString.indexOf(subString);
    }   
}
