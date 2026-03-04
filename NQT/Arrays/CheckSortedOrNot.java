import java.util.*;
public class CheckSortedOrNot {
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    //check if the array is sorted in non-decreasing order
    //check if the array is sorted in non-increasing order
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
        boolean isNonDecreasing = isSortedNonDecreasing(array);
        boolean isNonIncreasing = isSortedNonIncreasing(array);
        if (isNonDecreasing) {
            System.out.println("The array is sorted in non-decreasing order.");
        } else if (isNonIncreasing) {
            System.out.println("The array is sorted in non-increasing order.");
        } else {
            System.out.println("The array is not sorted.");
        }
    }

    // Function to check if the array is sorted in non-decreasing order
    //non-decreasing order means each element is greater than or equal to the previous one
    //increasing order
    private static boolean isSortedNonDecreasing(int[] array) {
        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1]) {
                return false; // Not sorted in non-decreasing order     
            }
        }
        return true; // Sorted in non-decreasing order  
    }

    // Function to check if the array is sorted in non-increasing order
    //non-increasing order means each element is less than or equal to the previous one
    //decreasing order
    private static boolean isSortedNonIncreasing(int[] array) {
        for (int i = 1; i < array.length; i++) {
            if (array[i] > array[i - 1]) {
                return false; // Not sorted in non-increasing order
            }
        }
        return true; // Sorted in non-increasing order
    }

}
