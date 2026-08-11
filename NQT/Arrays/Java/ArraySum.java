import java.util.*;
public class ArraySum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int sum_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            sum_list[i] = scanner.nextInt();
        }
        scanner.close();
        int sum = sum(sum_list, array_size);
        int sumInBuilt = sumInBuilt(sum_list, array_size);
        System.out.println("Sum using manual method: " + sum);
        System.out.println("Sum using in-built method: " + sumInBuilt);
    }
    private static int sum(int array[], int array_size){
        if(array_size == 0){
            return 0;
        }
        int sum = 0;
        for(int value: array){
            sum += value;
        }
        return sum;
    }

    //in-built method
    private static int sumInBuilt(int array[], int array_size){
        int sum = Arrays.stream(array).sum();
        return sum; 
    }
}
