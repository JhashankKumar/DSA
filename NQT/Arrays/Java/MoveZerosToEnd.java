public class MoveZerosToEnd {
    public static void main(String[] args) {
        int[] inputArray = {0, 1, 0, 3, 12};
        moveZerosToEnd(inputArray);
        System.out.println("Array after moving zeros to the end:");
        for (int num : inputArray) {
            System.out.print(num + " ");
        }
    }

    private static void moveZerosToEnd(int[] array) {
        int n = array.length;
        int writeIndex = 0;

        // Move all non-zero elements to the front
        for (int i = 0; i < n; i++) {
            if (array[i] != 0) {
                array[writeIndex] = array[i];
                writeIndex++;
            }
        }

        // Fill the remaining positions with zeros
        while (writeIndex < n) {
            array[writeIndex] = 0;
            writeIndex++;
        }
    }
}
