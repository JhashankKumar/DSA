package Numbers;

public class AtomorphicNumber {
    public static void main(String[] args) {
        int number = 25; // Example number
        if (isAtomorphic(number)) {
            System.out.println(number + " is an Atomorphic number.");
        } else {
            System.out.println(number + " is not an Atomorphic number.");
        }
    }
    
    private static boolean isAtomorphic(int number) {
        int square = number * number;
        String numberStr = String.valueOf(number);
        String squareStr = String.valueOf(square);
        return squareStr.endsWith(numberStr);
    }
}
