import java.util.*;
public class Average {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int average_list[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            average_list[i] = scanner.nextInt();
        }
        scanner.close();
        float average = average(average_list, array_size);
        System.out.println(average);
    }

    private static float average(int array[], int array_size){
    int sum = 0;
    for(int value: array){
        sum += value;
    }
    float average = (float)sum/array_size;
    return average;
    }
}
