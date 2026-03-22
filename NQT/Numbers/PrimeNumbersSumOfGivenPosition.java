package Numbers;

public class PrimeNumbersSumOfGivenPosition {
    // two postions are given, find the sum of prime numbers comes at those two
    // positions.
    public static void main(String[] args) {
        int position1 = 5;
        int position2 = 10;
        int sum = sumOfPrimeNumbersAtPositions(position1, position2);
        System.out.println("Sum of prime numbers at positions " + position1 + " and " + position2 + " is: " + sum);
    }

    private static int sumOfPrimeNumbersAtPositions(int position1, int position2) {
        int count = 0;
        int num = 2;
        int sum = 0;
        while (count < Math.max(position1, position2)) {
            if (isPrime(num)) {
                count++;
                if (count == position1 || count == position2) {
                    sum += num;
                }
            }
            num++;
        }
        return sum;
    }

    private static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}