package TrickyInputs.Java;

import java.util.Scanner;

public class MultiInputInOneLine {
    // 10 20 30
    public static void main(String[] args) {    
        // fixed number of inputs in one line
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter three integers separated by space:");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println("You entered: " + a + " " + b + " " + c);
        scanner.close();
    }
}
