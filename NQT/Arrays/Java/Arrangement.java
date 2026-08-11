import java.util.*;
public class Arrangement {
    // arrange the elements in array in both ascending and descending order
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int arrangement_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            arrangement_list[i] = scanner.nextInt();
        }
        scanner.close();
        int[] ascending = ascending(arrangement_list, array_size);
        int[] descending = descending(arrangement_list, array_size);
        System.out.println("Original array: " + Arrays.toString(arrangement_list));
        System.out.println("Ascending order: " + Arrays.toString(ascending));
        System.out.println("Descending order: " + Arrays.toString(descending));
    }
    private static int[] ascending(int array[], int array_size){
        Arrays.sort(array);
        return array;
    }
    private static int[] descending(int array[], int array_size){
        Arrays.sort(array);
        int descending_array[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            descending_array[i] = array[array_size - 1 - i];
        }
        return descending_array;
    }
}
