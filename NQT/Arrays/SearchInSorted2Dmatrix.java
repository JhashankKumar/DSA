import java.util.*;
public class SearchInSorted2Dmatrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of columns:");
        int cols = scanner.nextInt();
        int[][] matrix = new int[rows][cols];
        System.out.println("Enter " + (rows * cols) + " elements in sorted order:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        System.out.println("Enter the element to search:");
        int elementToSearch = scanner.nextInt();
        scanner.close();
        boolean found = searchElementInSortedMatrix(matrix, rows, cols, elementToSearch);
        if (found) {
            System.out.println("Element " + elementToSearch + " found in the matrix.");
        } else {
            System.out.println("Element " + elementToSearch + " not found in the matrix."); 
        }
    }
    
    // Time Complexity: O(rows + cols)
    // Space Complexity: O(1)
    private static boolean searchElementInSortedMatrix(int[][] matrix, int rows, int cols, int element) {
        int row = 0;
        int col = cols - 1;
        while (row < rows && col >= 0) {
            if (matrix[row][col] == element) {
                return true;
            } else if (matrix[row][col] > element) {
                col--; // Move left
            } else {
                row++; // Move down
            }
        }
        return false;
    }
}
