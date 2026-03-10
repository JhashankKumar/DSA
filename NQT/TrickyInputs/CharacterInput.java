package TrickyInputs;
import java.util.*;
public class CharacterInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a character:");
        char ch = scanner.next().charAt(0);
        System.out.println("You entered: " + ch);
        scanner.close();
    }
}
