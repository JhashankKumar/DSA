package NumberSystem;

public class DecimalToOctal {
    public static void main(String[] args) {
        int decimalNumber = 45; // You can change this value to test with different decimal numbers
        String octalValue = decimalToOctal(decimalNumber);
        System.out.println("The octal value of decimal " + decimalNumber + " is: " + octalValue);
    }

    private static String decimalToOctal(int decimal) {
        if (decimal == 0) {
            return "0";
        }
        StringBuilder octalValue = new StringBuilder();
        while (decimal > 0) {
            int remainder = decimal % 8;
            octalValue.insert(0, remainder); // Prepend the remainder to the octal string
            decimal /= 8; // Divide the decimal number by 8
        }
        return octalValue.toString();
    }
}
