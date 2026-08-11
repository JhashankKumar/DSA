import java.io.*;

public class BinaryRowMax1s {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the number of rows:");
        int rows = Integer.parseInt(reader.readLine());
        System.out.println("Enter the number of columns:");
        int cols = Integer.parseInt(reader.readLine());
        int[][] matrix = new int[rows][cols];
        System.out.println("Enter the binary matrix (0s and 1s):");
        for (int i = 0; i < rows; i++) {
            String[] input = reader.readLine().split(" ");
            for (int j = 0; j < cols; j++) { 
                matrix[i][j] = Integer.parseInt(input[j]);
            }
        }
        reader.close();
        int maxOnesRowIndex = findRowWithMaxOnes(matrix, rows, cols);
        if (maxOnesRowIndex != -1) {
            System.out.println("Row with maximum number of 1s: " + maxOnesRowIndex);
        } else {
            System.out.println("No row contains 1s.");
        }
    }

    private static int findRowWithMaxOnes(int[][] matrix, int rows, int cols) {
        int maxOnesRowIndex = -1;
        int maxOnesCount = 0;
        for (int i = 0; i < rows; i++) {
            int onesCount = countOnesInRow(matrix[i], cols);
            if (onesCount > maxOnesCount) {
                maxOnesCount = onesCount;
                maxOnesRowIndex = i;
            }
        }
        return maxOnesRowIndex;
    }

    private static int countOnesInRow(int[] row, int cols) {
        int count = 0;
        for (int j = 0; j < cols; j++) {
            if (row[j] == 1) {
                count++;
            }
        }
        return count;
    }
}
