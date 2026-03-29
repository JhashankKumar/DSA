public class MaxElementInSubArray {
    public static void main(String[] args) {
        int[] array = {1, 3, 2, 5, 4};
        int k = 3; // Size of the subarray
        System.out.println("Maximum elements in each subarray of size " + k + ":");
        findMaxInSubArrays(array, k);
    }

    private static void findMaxInSubArrays(int[] array, int k) {
        int n = array.length;
        for (int i = 0; i <= n - k; i++) {
            int max = array[i];
            for (int j = i + 1; j < i + k; j++) {
                if (array[j] > max) {
                    max = array[j];
                }
            }
            System.out.print(max + " ");
        }
    }   

    // function that return in array of maximum elements in each subarray of size k
    private static int[] findMaxInSubArraysOptimized(int[] array, int k) {
        int n = array.length;
        int[] maxInSubArrays = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            int max = array[i];
            for (int j = i + 1; j < i + k; j++) {
                if (array[j] > max) {
                    max = array[j]; 
                }
            }
            maxInSubArrays[i] = max;
        }
        return maxInSubArrays;
    }
}
