import java.util.*;

// Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d.
// For example, (1, 2) and (2, 1) are symmetric pairs, but (1, 2) and (3, 4) are not.
// use a hash map to store the pairs and check for symmetric pairs
public class SymmetricPairs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int symmetric_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            symmetric_list[i] = scanner.nextInt();
        }
        scanner.close();
        System.out.println("Symmetric pairs:");
        findSymmetricPairs(symmetric_list);
    }

    private static void findSymmetricPairs(int array[]) {
        HashMap<Integer, Integer> pairMap = new HashMap<>();
        for (int i = 0; i < array.length; i += 2) {
            int a = array[i];
            int b = array[i + 1];
            pairMap.put(a, b);
        }
        for (int a : pairMap.keySet()) {
            int b = pairMap.get(a);
            if (pairMap.containsKey(b) && pairMap.get(b) == a) {
                System.out.println("(" + a + ", " + b + ")");
            }
        }
    }
}
 