public class RemoveBrackets {
    public static void main(String[] args) {
        String input = "Hello (World) [Java] {Programming}";
        String result = removeBrackets(input);
        System.out.println(result);
    }

    private static String removeBrackets(String input) {
        return input.replaceAll("[\\(\\)\\[\\]\\{\\}]", "");
    }
}
