package NumberSystem;

public class BinaryToDecimal {
    public static void main(String[] args) {
        String binaryString = "1011"; // You can change this value to test with different binary numbers
        int decimalValue = binaryToDecimal(binaryString);
        System.out.println("The decimal value of binary " + binaryString + " is: " + decimalValue);
    }

    private static int binaryToDecimal(String binary) {
        int decimalValue = 0;
        int length = binary.length();
        for (int i = 0; i < length; i++) {
            char bit = binary.charAt(length - 1 - i);
            if (bit == '1') {
                decimalValue += Math.pow(2, i);
            }
        }
        return decimalValue;
    }
}
