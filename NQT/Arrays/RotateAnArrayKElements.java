import java.util.*;
public class RotateAnArrayKElements {
    //Array Rotation using Array Reversal
    //Time Complexity: O(n)
    //Space Complexity: O(1)
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int array[] = new int[array_size];
        for (int i = 0; i < array_size; i++) {
            array[i] = scanner.nextInt();
        }
        System.out.println("Enter the number of positions to rotate:");
        int k = scanner.nextInt();
        scanner.close();
        rotateArray(array, k);
        System.out.println("Rotated array:");
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println(); // Print a newline for better formatting
    }

    private static void rotateArray(int[] array, int k) {
        int n = array.length;
        k = k % n; // Handle cases where k is greater than n
        reverse(array, 0, n - 1); // Reverse the entire array
        reverse(array, 0, k - 1); // Reverse the first k elements
        reverse(array, k, n - 1); // Reverse the remaining n-k elements
    }

    private static void reverse(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    } 
}