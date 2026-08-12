package Numbers.Java;

public class FactorsOfNumber {
    public static void main(String[] args) {
        int number = 12; // Example number
        System.out.println("Factors of " + number + " are:");
        for (int i = 1; i <= number; i++) {
            if (number % i == 0) {
                System.out.println(i);
            }
        }
    }
}
