import java.util.*;
public class Median {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int median_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            median_list[i] = scanner.nextInt();
        }
        scanner.close();
        float median = median(median_list, array_size);
        System.out.println(median);
    }

    private static float median(int array[], int array_size){
    Arrays.sort(array);
    if(array_size % 2 == 0){
        return (float)(array[array_size/2 - 1] + array[array_size/2])/2;
    } else {
        return (float)array[array_size/2];
    }
    }
    
}
