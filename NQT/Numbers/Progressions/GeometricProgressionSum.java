package Numbers.Progressions;

public class GeometricProgressionSum {

    public static void main(String[] args) {
        int firstTerm = 2; // First term of the progression
        int commonRatio = 3; // Common ratio
        int numberOfTerms = 5; // Number of terms to generate

        int sum = calculateGPSum(firstTerm, commonRatio, numberOfTerms);
        int sumUsingLoop = calculateGPSumUsingLoop(firstTerm, commonRatio, numberOfTerms);
        System.out.println("The sum of the first " + numberOfTerms + " terms of the geometric progression is: " + sum);
        System.out.println("The sum of the first " + numberOfTerms + " terms of the geometric progression (using loop) is: " + sumUsingLoop);
    }

    private static int calculateGPSum(int firstTerm, int commonRatio, int numberOfTerms) {
        // Using the formula: S_n = a * (r^n - 1) / (r - 1) for r != 1
        if (commonRatio == 1) {
            return firstTerm * numberOfTerms; // If r is 1, all terms are the same
        }
        return (int) (firstTerm * (Math.pow(commonRatio, numberOfTerms) - 1) / (commonRatio - 1));
    }

    // Alternatively, you can calculate the sum using a loop:
    private static int calculateGPSumUsingLoop(int firstTerm, int commonRatio, int numberOfTerms) {
        int sum = 0;
        for (int i = 0; i < numberOfTerms; i++) {
            sum += firstTerm * Math.pow(commonRatio, i);
            System.out.print("Term " + (i + 1) + ": " + (firstTerm * Math.pow(commonRatio, i))); // Print each term
        }
        return sum; 
    }
}