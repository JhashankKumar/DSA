package NumberSystem.Java;

public class DecimalToBinary {
    public static void main(String[] args) {
        int decimalNumber = 45; // You can change this value to test with different decimal numbers
        String binaryValue = decimalToBinary(decimalNumber);
        System.out.println("The binary value of decimal " + decimalNumber + " is: " + binaryValue);
    }

    private static String decimalToBinary(int decimal) {
        if (decimal == 0) {
            return "0";
        }
        StringBuilder binaryValue = new StringBuilder();
        while (decimal > 0) {
            int remainder = decimal % 2;
            binaryValue.insert(0, remainder); // Prepend the remainder to the binary string
            decimal /= 2; // Divide the decimal number by 2
        }
        return binaryValue.toString();
    }
}
