import java.util.*;

public class LargestAndSmallestInArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int largest_list[] = new int[array_size];
        for (int i = 0; i < array_size; i++) {
            largest_list[i] = scanner.nextInt();
        }
        scanner.close();
        int largest = largest(largest_list, array_size);
        int smallest = smallest(largest_list, array_size);
        System.out.println("Smallest: " + smallest);
        System.out.println("Largest: " + largest);
    }

    private static int largest(int array[], int array_size) {
        int largest = Integer.MIN_VALUE;
        for (int value : array) {
            if (value > largest) {
                largest = value;
            }
        }
        return largest;
    }

    private static int smallest(int array[], int array_size) {
        int smallest = Integer.MAX_VALUE;
        for (int value : array) {
            if (value < smallest) {
                smallest = value;
            }
        }
        return smallest;
    }
}
