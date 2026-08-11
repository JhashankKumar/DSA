package NumberSystem.Java;

public class OctalToBinary {
    public static void main(String[] args) {
        String octalString = "17"; // You can change this value to test with different octal numbers
        String binaryValue = octalToBinary(octalString);
        System.out.println("The binary value of octal " + octalString + " is: " + binaryValue);
    }

    private static String octalToBinary(String octal) {
        StringBuilder binaryValue = new StringBuilder();
        for (char digit : octal.toCharArray()) {
            int octalDigit = Character.getNumericValue(digit);
            String binaryDigits = String.format("%3s", Integer.toBinaryString(octalDigit)).replace(' ', '0');
            binaryValue.append(binaryDigits);
        }
        return binaryValue.toString();
    }
}
