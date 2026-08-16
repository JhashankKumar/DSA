public class RemoveSpaces {
    public static void main(String[] args) {
        String input = "  Hello   World!  ";
        String output = removeSpaces(input);
        System.out.println("Original String: '" + input + "'");
        System.out.println("String after removing spaces: '" + output + "'");
    }

    private static String removeSpaces(String string) {
        return string.replaceAll("\\s+", "");
    }
}
