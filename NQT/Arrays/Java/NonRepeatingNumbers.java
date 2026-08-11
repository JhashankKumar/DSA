import java.util.*;

public class NonRepeatingNumbers {
    // This method finds and prints the non-repeating numbers in the given array
    // Time Complexity: O(n) where n is the size of the array
    // using HashMap to store the frequency of each number in the array
    public static void findNonRepeatingNumbers(int[] array) {
        System.out.println("Non-repeating numbers in the array:");
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        // Count the frequency of each number in the array
        for (int num : array) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        // Print the numbers that have a frequency of 1 (non-repeating)
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() == 1) {
                System.out.print(entry.getKey() + " ");
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();
        int[] array = new int[size];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }
        scanner.close();
        findNonRepeatingNumbers(array);
    }
}
