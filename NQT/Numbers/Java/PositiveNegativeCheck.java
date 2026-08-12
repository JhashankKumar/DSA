package Numbers.Java;

public class PositiveNegativeCheck {
    public static void main(String[] args) {
        int number = -5; // You can change this value to test with different numbers

        if (number > 0) {
            System.out.println(number + " is a positive number.");
        } else if (number < 0) {
            System.out.println(number + " is a negative number.");
        } else {
            System.out.println("The number is zero.");
        }
    }
}
