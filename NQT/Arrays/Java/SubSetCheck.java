import java.util.*;
public class SubSetCheck{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // Input for array 1
        System.out.println("Enter the size of the first array:");
        int array_1_size = scanner.nextInt();
        System.out.println("Enter " + array_1_size + " integers for the first array:");
        int array_1[] = new int[array_1_size];  
        for(int i = 0;i<array_1_size;i++){
            array_1[i] = scanner.nextInt();
        }
        // Input for array 2
        System.out.println("Enter the size of the second array:");
        int array_2_size = scanner.nextInt();
        System.out.println("Enter " + array_2_size + " integers for the second array:");
        int array_2[] = new int[array_2_size];
        for(int i = 0;i<array_2_size;i++){
            array_2[i] = scanner.nextInt();
        }
        scanner.close();
        boolean isSubset = isSubset(array_1, array_2, array_1_size, array_2_size);
        System.out.println("isSubset: " + isSubset);
    }
    private static boolean isSubset(int array_1[], int array_2[], int array_1_size, int array_2_size){
        Set<Integer> set_1 = new HashSet<>();
        Set<Integer> set_2 = new HashSet<>();   
        for(int i = 0;i<array_1_size;i++){
            set_1.add(array_1[i]);
        }
        for(int i = 0; i<array_2_size;i++){
            set_2.add(array_2[i]);
        }
        return set_1.containsAll(set_2);
    }
}