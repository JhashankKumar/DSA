import java.util.*;
public class SecondLargestAndSmallestInArray {
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
        int second_largest = secondLargest(largest_list, array_size);
        int second_smallest = secondSmallest(largest_list, array_size);
        System.out.println("Second Smallest: " + second_smallest);
        System.out.println("Second Largest: " + second_largest);
    }
    private static int secondLargest(int array[], int array_size) {
        int largest = Integer.MIN_VALUE;
        int second_largest = Integer.MIN_VALUE;
        for (int value : array) {
            if (value > largest) {
                second_largest = largest;
                largest = value;
            } else if (value > second_largest && value != largest) {
                second_largest = value;
            }
        }
        return second_largest;
    }
    private static int secondSmallest(int array[], int array_size) {
        int smallest = Integer.MAX_VALUE;
        int second_smallest = Integer.MAX_VALUE;
        for (int value : array) {
            if (value < smallest) {
                second_smallest = smallest;
                smallest = value;
            } else if (value < second_smallest && value != smallest) {
                second_smallest = value;
            }
        }
        return second_smallest;
    }
}
