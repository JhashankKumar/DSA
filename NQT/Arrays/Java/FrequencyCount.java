import java.util.*;

public class FrequencyCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int frequency_list[] = new int[array_size];
        for (int i = 0; i < array_size; i++) {
            frequency_list[i] = scanner.nextInt();
        }
        scanner.close();
        Map<Integer, Integer> frequencyMap = frequencyCount(frequency_list, array_size);
        int most_frequent = Collections.max(frequencyMap.entrySet(), Map.Entry.comparingByValue()).getKey();
        System.out.println("Most frequent element: " + most_frequent);
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    private static Map<Integer, Integer> frequencyCount(int array[], int array_size) {
        // Step 1 - Create a HashMap to store the frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int value : array) {
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }

        // step 2 - convert the HashMap to a List of Map.Entry objects and sort it by
        // frequency in descending order
        List<Map.Entry<Integer, Integer>> sortedEntries = new ArrayList<>(frequencyMap.entrySet());
        sortedEntries.sort((entry1, entry2) -> {
            if (!entry1.getValue().equals(entry2.getValue())) {
                return entry2.getValue().compareTo(entry1.getValue());
            }
            return entry1.getKey().compareTo(entry2.getKey());
        });

        // Step 3 - Create a LinkedHas hMap to maintain the sorted order of elements
        Map<Integer, Integer> sortedFrequencyMap = new LinkedHashMap<>();
        for (Map.Entry<Integer, Integer> entry : sortedEntries) {
            sortedFrequencyMap.put(entry.getKey(), entry.getValue());
        }
        return sortedFrequencyMap;
    }
}
