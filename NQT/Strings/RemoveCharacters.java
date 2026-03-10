public class RemoveCharacters {
    public static void main(String[] args) {
        String input = "Hello World!";
        String charactersToRemove = "lo";
        String output = removeCharacters(input, charactersToRemove);
        System.out.println("Original String: " + input);
        System.out.println("String after removing characters '" + charactersToRemove + "': " + output);
    }

    private static String removeCharacters(String input, String charactersToRemove) {
        StringBuilder result = new StringBuilder();
        for (char c : input.toCharArray()) {
            if (charactersToRemove.indexOf(c) == -1) {
                result.append(c);
            }
        }
        return result.toString(); 
    }
}
