package TrickyInputs.Java;

import java.util.*;

public class StringInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string:");
        String input = scanner.nextLine();
        System.out.println("You entered: " + input);
        scanner.close();

        //if using nextInt() before nextLine()
        System.out.println("Enter a number:");
        int num = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter a string after the number:");
        String strAfterNum = scanner.nextLine();
        System.out.println("You entered number: " + num);
        System.out.println("You entered string: " + strAfterNum);
        scanner.close();
    }
}
