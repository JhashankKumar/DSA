package TrickyInputs.Java;
import java.util.*;
public class InputUntilEOF {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter integers (press Ctrl+D to end input):");
        while (scanner.hasNextInt()) {
            int num = scanner.nextInt();
            System.out.println("You entered: " + num);
        }
        System.out.println("End of input reached.");
        scanner.close();
    }
}
