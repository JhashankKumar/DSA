package TrickyInputs.Java;
import java.util.*;

public class CommaSeperatedInput {
    public static void main(String[] args) {
        //no size specified in input, just comma seperated values
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter comma-separated integers:");
        String input = scanner.nextLine();
        String[] inputArr = input.split(",");
        int[] arr = new int[inputArr.length];
        for (int i = 0; i < inputArr.length; i++) {
            arr[i] = Integer.parseInt(inputArr[i].trim());
        }
        System.out.println("You entered the array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
        scanner.close();
    }
}
