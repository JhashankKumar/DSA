import java.util.*;
public class SumOfNumbers {
    //input format 
     /**
     * Multiple consecutive digits are considered one number 
     * ex. 12abc#12    -> sum is = 12+12=24 
     * */

     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int sum = 0;
        StringBuilder currentNumber = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (Character.isDigit(c)) {
                currentNumber.append(c);
            } else {
                if (currentNumber.length() > 0) {
                    sum += Integer.parseInt(currentNumber.toString());
                    currentNumber.setLength(0); // Clear the StringBuilder
                }
            }
        }
        scanner.close();

        // Check if there's a number at the end of the string
        if (currentNumber.length() > 0) {
            sum += Integer.parseInt(currentNumber.toString());
        }

        System.out.println("Sum of numbers: " + sum);
    }

}
