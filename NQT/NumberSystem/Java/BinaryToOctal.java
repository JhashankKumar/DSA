package NumberSystem.Java;

public class BinaryToOctal {
    public static void main(String[] args) {
        String binaryString = "101101"; // You can change this value to test with different binary numbers
        String octalValue = binaryToOctal(binaryString);
        System.out.println("The octal value of binary " + binaryString + " is:  " + octalValue);
    }

    private static String binaryToOctal(String binary) {
        // Pad the binary string with leading zeros to make its length a multiple of 3
        int paddingLength = (3 - (binary.length() % 3)) % 3;
        String paddedBinary = "0".repeat(paddingLength) + binary;

        StringBuilder octalValue = new StringBuilder();
        for (int i = 0; i < paddedBinary.length(); i += 3) {
            String threeBits = paddedBinary.substring(i, i + 3);
            int octalDigit = Integer.parseInt(threeBits, 2);
            octalValue.append(octalDigit);
        }
        return octalValue.toString();
    }
}
