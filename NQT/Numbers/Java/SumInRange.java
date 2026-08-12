package Numbers.Java;

public class SumInRange {
    // This program calculates the sum of all numbers in a given range (inclusive).

    public static void main(String[] args) {
        int start = 1; // Starting number of the range
        int end = 10; // Ending number of the range

        int sum = calculateSumInRange(start, end);
        System.out.println("The sum of numbers from " + start + " to " + end + " is: " + sum);
    }

    private static int calculateSumInRange(int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            sum += i;
        }
        return sum;
    }

    // Alternatively, you can use the formula for the sum of the first n natural numbers:
    private static int calculateSumInRangeUsingFormula(int start, int end) {
        return (end * (end + 1)) / 2 - ((start - 1) * start) / 2;
    }
}
