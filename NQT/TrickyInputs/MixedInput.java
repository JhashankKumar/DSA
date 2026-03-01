package NQT.TrickyInputs;

import java.util.Scanner;

public class MixedInput {
    /*
     3
     Ramesh 85
     Suresh 90
     Mahesh 75 
    */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of students:");
        int numStudents = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after nextInt()
        String[] names = new String[numStudents];
        int[] marks = new int[numStudents];
        for (int i = 0; i < numStudents; i++) {
            System.out.println("Enter name and marks for student " + (i + 1) + " (e.g., Ramesh 85):");
            String input = scanner.nextLine();
            String[] parts = input.split(" ");
            names[i] = parts[0];
            marks[i] = Integer.parseInt(parts[1]);  
        }
        System.out.println("Student Details:");
        for (int i = 0; i < numStudents; i++) {
            System.out.println(names[i] + " " + marks[i]);
        }
    }
}
