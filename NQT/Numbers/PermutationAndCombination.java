package Numbers;

public class PermutationAndCombination {
    public static void main(String[] args) {
        int n = 5;
        int r = 3;

        System.out.println("Permutation (nPr): " + permutation(n, r));
        System.out.println("Combination (nCr): " + combination(n, r));
    }

    // Function to calculate factorial
    public static long factorial(int num) {
        if (num == 0 || num == 1) {
            return 1;
        }
        long fact = 1;
        for (int i = 2; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }

    // Function to calculate permutation (nPr)
    public static long permutation(int n, int r) {
        if (r > n) {
            return 0; // Not possible to choose more elements than available
        }
        return factorial(n) / factorial(n - r);
    }

    // Function to calculate combination (nCr)
    public static long combination(int n, int r) {
        if (r > n) {
            return 0; // Not possible to choose more elements than available
        }
        return factorial(n) / (factorial(r) * factorial(n - r));
    }
}