import java.util.*;
public class EquilibriumIndex {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int equilibrium_list [] = new int[array_size];
        for (int i = 0; i < array_size; i++) {
            equilibrium_list[i] = scanner.nextInt();
        }
        scanner.close();
        //calculate sum of all elements in the array from left and store in left_sum array
        int left_sum[] = new int[array_size];
        left_sum[0] = equilibrium_list[0];
        for (int i = 1; i < array_size; i++) {
            left_sum[i] = left_sum[i - 1] + equilibrium_list[i];
        }
        //calculate sum of all elements in the array from right and store in right_sum array
        int right_sum[] = new int[array_size];
        right_sum[array_size - 1] = equilibrium_list[array_size - 1];
        for (int i = array_size - 2; i >= 0; i--) {
            right_sum[i] = right_sum[i + 1] + equilibrium_list[i];
        }
        //find equilibrium index
        for (int i = 0; i < array_size; i++) {
            if (left_sum[i] == right_sum[i]) {
                System.out.println("Equilibrium index: " + i);
                return;
            }
        }
        System.out.println("No equilibrium index found.");
    }
}
