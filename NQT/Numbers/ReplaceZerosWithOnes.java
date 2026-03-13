package Numbers;

public class ReplaceZerosWithOnes {
    public static void main(String[] args) {
        int number = 1020304050; // You can change this value to test with different numbers
        String modifiedNumber = replaceZerosWithOnes(number);
        System.out.println("Original number: " + number);
        System.out.println("Modified number: " + modifiedNumber);
    }

    private static String replaceZerosWithOnes(int number) {
        // String numberStr = Integer.toString(number);
        String numberStr = String.valueOf(number);
        return numberStr.replace('0', '1');
    }
}
