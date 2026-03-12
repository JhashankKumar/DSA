package Numbers;

public class EvenOrNot {
    public static void main(String[] args) {
        int number = 10; // Example number
        if (isEven(number)) {
            System.out.println(number + " is an even number.");
        } else {
            System.out.println(number + " is not an even number.");
        }
    }

    private static boolean isEven(int number) {
        return number % 2 == 0;
    }
}
