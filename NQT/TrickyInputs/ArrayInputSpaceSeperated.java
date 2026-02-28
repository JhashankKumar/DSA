package NQT.TrickyInputs;
import java.util.*;
public class ArrayInputSpaceSeperated {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter " + size + " space-separated integers:");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }
        System.out.println("You entered the array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
        scanner.close();
    }
}
