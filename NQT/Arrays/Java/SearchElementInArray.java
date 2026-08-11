import java.util.*;

public class SearchElementInArray {
    public static void main(String[] args) {
        // search for an element in an array of integers
        //method 1 linear search
        //method 2 binary search (array must be sorted)
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();
        int[] array = new int[size];
        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {    
            array[i] = scanner.nextInt(); 
        }
        System.out.println("Enter the element to search:");
        int elementToSearch = scanner.nextInt();
        scanner.close();
        int linearIndex = LinearSearch(array, elementToSearch);
        int BinaryIndex = BinarySearch(array, elementToSearch);
        if (linearIndex != -1) {
            System.out.println("Element " + elementToSearch + " found at index: " + linearIndex);
        } else {
            System.out.println("Element " + elementToSearch + " not found in the array.");
        }
        if (BinaryIndex != -1) {
            System.out.println("Element " + elementToSearch + " found at index: " + BinaryIndex);
        } else {
            System.out.println("Element " + elementToSearch + " not found in the array.");
        }
    }

    private static int LinearSearch(int[] array, int elementToSearch) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == elementToSearch) {
                return i;
            }
        }
        return -1;
    }

    private static int BinarySearch(int[] array, int elementToSearch) {
        int left = 0;
        int right = array.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2; 
            if (array[mid] == elementToSearch) {
                return mid;
            } else if (array[mid] < elementToSearch) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
