import java.util.*;
public class FrequencyCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int frequency_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            frequency_list[i] = scanner.nextInt();
        }
        scanner.close();
        Map<Integer, Integer> frequencyMap = frequencyCount(frequency_list, array_size);
        int most_frequent = Collections.max(frequencyMap.entrySet(), Map.Entry.comparingByValue()).getKey();
        System.out.println("Most frequent element: " + most_frequent);
        for(Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()){
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    private static Map<Integer, Integer> frequencyCount(int array[], int array_size){
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for(int value: array){
            frequencyMap.put(value, frequencyMap.getOrDefault(value, 0) + 1);
        }
        return frequencyMap;
    }
}
