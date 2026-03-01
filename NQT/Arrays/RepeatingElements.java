import java.util.*;
public class RepeatingElements {
    // Function to find and print repeating elements and non-repeating elements in an array
    public static void findRepeatingAndNonRepeating(int[] arr) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        System.out.println("Repeating elements:");
        for (int num : frequencyMap.keySet()) {
            if (frequencyMap.get(num) > 1) {
                System.out.print(num + " ");
            }
        }
        System.out.println("\nNon-repeating elements:");
        for (int num : frequencyMap.keySet()) {
            if (frequencyMap.get(num) == 1) {
                System.out.print(num + " ");
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }
        scanner.close();
        findRepeatingAndNonRepeating(arr);
    }
}