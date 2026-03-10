import java.util.*;
public class ReplaceElementsByRank {
    private static int[] replaceElementsByRank(int[] array  ) {
        int n = array.length;
        int[] sortedArray = Arrays.copyOf(array, n);
        Arrays.sort(sortedArray);
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            rankMap.put(sortedArray[i], i + 1); // Rank starts from 1
        }
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = rankMap.get(array[i]);
        }
        return result;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();
        int[] array = new int[size];
        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }
        scanner.close();
        int arrayCopy[] = Arrays.copyOf(array, size);
        int[] result = replaceElementsByRank(arrayCopy);
        System.out.println("Array after replacing elements by their rank:");
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
