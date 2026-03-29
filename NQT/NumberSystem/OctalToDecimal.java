package NumberSystem;

public class OctalToDecimal {
    public static void main(String[] args) {
        String octalString = "17"; // You can change this value to test with different octal numbers
        int decimalValue = octalToDecimal(octalString);
        System.out.println("The decimal value of octal " + octalString + " is: " + decimalValue);
    }

    private static int octalToDecimal(String octal) {
        int decimalValue = 0;
        int length = octal.length();
        for (int i = 0; i < length; i++) {
            char digit = octal.charAt(length - 1 - i);
            int octalDigit = Character.getNumericValue(digit);
            decimalValue += octalDigit * Math.pow(8, i);
        }
        return decimalValue;
    }
}
