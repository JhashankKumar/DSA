public class SubArray {
    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4 };
        System.out.println("Subarrays of the given array:");
        printSubArrays(array);
    }

    // Time Complexity: O(n^3) due to three nested loops
    // Space Complexity: O(1) as we are not using any extra space
    private static void printSubArrays(int[] array) {
        int n = array.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // Print subarray from index i to j
                for (int k = i; k <= j; k++) {
                    System.out.print(array[k] + " ");
                }
                System.out.println(); // New line after each subarray
            }
        }
    }

    // Time Complexity: O(n^2) due to two nested loops
    // Space Complexity: O(1) as we are not using any extra space
    private static void printSubArraysOptimized(int[] array) {
        int n = array.length;
        for (int i = 0; i < n; i++) {
            StringBuilder subArray = new StringBuilder();
            for (int j = i; j < n; j++) {
                subArray.append(array[j]).append(" ");
                System.out.println(subArray.toString().trim()); // Print current subarray
            }
        }
    }
}