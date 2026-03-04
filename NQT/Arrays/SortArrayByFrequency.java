import java.util.*;

public class SortArrayByFrequency {
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
        // sortByFrequencyUsingHashMap(array);
        sortByFrequencyUsingArrayList(array);
        System.out.println("Array sorted by frequency:");
        for (int value : array) {
            System.out.print(value + " ");
        }
    }

    //using hashmap to count frequency and then sorting the array based on frequency
    private static void sortByFrequencyUsingHashMap(int[] array) {
        // Count frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int value : array) {
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }
        // Convert to Integer array for sorting with comparator
        Integer[] integerArray = new Integer[array.length];
        for (int i = 0; i < array.length; i++) {
            integerArray[i] = array[i];
        }
        // Sort the array based on frequency and then by value
        Arrays.sort(integerArray, (a, b) -> {
            int freqCompare = Integer.compare(frequencyMap.get(a), frequencyMap.get(b));
            if (freqCompare == 0) {
                return Integer.compare(a, b); // If frequencies are equal, sort by value
            }
            return freqCompare; // Sort by frequency
        });
        // Convert back to primitive array
        for (int i = 0; i < array.length; i++) {
            array[i] = integerArray[i];
        }
    }

    //using ArrayList to count frequency and then sorting the array based on frequency
    private static void sortByFrequencyUsingArrayList(int[] array) {
       Map <Integer, Integer> frequencyMap = new HashMap<>();
        for (int value : array) {
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(frequencyMap.entrySet());
        Collections.sort(list, (a, b) -> {
            int freqCompare = Integer.compare(b.getValue(), a.getValue()); // Sort by frequency descending
            if (freqCompare == 0) {
                return Integer.compare(a.getKey(), b.getKey()); // If frequencies are equal, sort by value ascending
            }
            return freqCompare;
        });
        int index = 0;
        for (Map.Entry<Integer, Integer> entry : list) {
            for (int i = 0; i < entry.getValue(); i++) {
                array[index++] = entry.getKey();
            }
        }

    }
}
