import java.util.Scanner;

public class MaxSubArraySumProduct {
    // Given an array of integers, find the maximum product of a subarray.
    //use kadane's algorithm to find the maximum product of a subarray
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int array[] = new int[array_size];
        for (int i = 0; i < array_size; i++) {
            array[i] = scanner.nextInt();
        }
        scanner.close();
        int maxProduct = maxProductSubArray(array);
        System.out.println("Maximum product of a subarray is: " + maxProduct); 
        int maxSum = maxSumSubArray(array);
        System.out.println("Maximum sum of a subarray is: " + maxSum);
    }

    private static int maxProductSubArray(int[] array) {
        int maxProduct = Integer.MIN_VALUE;
        int currentProduct = 1;
        for (int value : array) {
            currentProduct *= value;
            maxProduct = Math.max(maxProduct, currentProduct);
            if (currentProduct == 0) {
                currentProduct = 1; // Reset product if it becomes zero
            }
        }
        return maxProduct;
    }

    private static int maxSumSubArray(int[] array) {
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;
        for (int value : array) {
            currentSum += value;
            maxSum = Math.max(maxSum, currentSum);
            if (currentSum < 0) {
                currentSum = 0; // Reset sum if it becomes negative
            }
        }
        return maxSum;
    }
}
