import java.util.*;
public class SearchIn2Dmatrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of columns:");
        int cols = scanner.nextInt();
        int[][] matrix = new int[rows][cols];
        System.out.println("Enter " + (rows * cols) + " elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        System.out.println("Enter the element to search:");
        int elementToSearch = scanner.nextInt();
        scanner.close();
        boolean found = searchElementInMatrix(matrix, rows, cols, elementToSearch);
        if (found) {
            System.out.println("Element " + elementToSearch + " found in the matrix.");
        } else {
            System.out.println("Element " + elementToSearch + " not found in the matrix."); 
        }
    }
    // Time Complexity: O(rows * cols)
    // Space Complexity: O(1)
    private static boolean searchElementInMatrix(int[][] matrix, int rows, int cols, int element) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == element) {
                    return true;
                }
            }
        }
        return false;
    }
}
