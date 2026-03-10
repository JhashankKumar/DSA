package TrickyInputs;

import java.util.*;

public class InputInOneLine {
    public static void main(String[] args) {
        // Example: 10 20 30 40 50 (dymamic input size)
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter space-separated integers:");
        String input = scanner.nextLine();
        String[] tokens = input.split("\\s+");
        int[] numbers = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            numbers[i] = Integer.parseInt(tokens[i]);
        }
        System.out.println("You entered the numbers:");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
        scanner.close();
    }

}