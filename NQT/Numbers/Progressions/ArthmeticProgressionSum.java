package Numbers.Progressions;

public class ArthmeticProgressionSum {
    public static void main(String[] args) {
        int firstTerm = 1; // First term of the arithmetic progression
        int commonDifference = 2; // Common difference
        int numberOfTerms = 5; // Number of terms to sum

        int sum = calculateAPSum(firstTerm, commonDifference, numberOfTerms);
        int sumUsingLoop = calculateAPSumUsingLoop(firstTerm, commonDifference, numberOfTerms);
        System.out.println("The sum of the first " + numberOfTerms + " terms of the arithmetic progression is: " + sum);
        System.out.println("The sum of the first " + numberOfTerms + " terms of the arithmetic progression (using loop) is: " + sumUsingLoop); 
    }

    private static int calculateAPSum(int firstTerm, int commonDifference, int numberOfTerms) {
        // Using the formula: S_n = n/2 * (2a + (n-1)d)
        return (numberOfTerms / 2) * (2 * firstTerm + (numberOfTerms - 1) * commonDifference);
    }

    // Alternatively, you can calculate the sum using a loop:
    private static int calculateAPSumUsingLoop(int firstTerm, int commonDifference, int numberOfTerms) {
        int sum = 0;
        for (int i = 0; i < numberOfTerms; i++) {
            sum += firstTerm + i * commonDifference;
            System.out.print("Term " + (i + 1) + ": " + (firstTerm + i * commonDifference)); // Print each term
        }
        return sum;
    }
}
