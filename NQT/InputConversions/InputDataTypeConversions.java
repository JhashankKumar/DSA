package InputConversions;
import java.util.*;

public class InputDataTypeConversions {
    
    public static void main(String[] args) {
        // Example of converting a String to an integer
        String numberString = "123";
        int number = Integer.parseInt(numberString);
        System.out.println("The integer value is: " + number);

        // Example of converting a String to a double
        String doubleString = "3.14";
        double pi = Double.parseDouble(doubleString);
        System.out.println("The double value is: " + pi);

        // Example of converting an integer to a String
        int age = 30;
        String ageString = Integer.toString(age);
        System.out.println("The age as a string is: " + ageString);

        // Example of converting a double to a String
        double temperature = 36.6;
        String temperatureString = Double.toString(temperature);
        System.out.println("The temperature as a string is: " + temperatureString);
    }

    // Array -> ArrayList conversion
    //for string array to arraylist
    private static void arrayToArrayList() {
        String[] array = {"Apple", "Banana", "Cherry"};
        List<String> arrayList = new ArrayList<>(Arrays.asList(array));
        System.out.println("ArrayList: " + arrayList);
    }

    //for integer array to arraylist
    private static void intArrayToArrayList() {
        int[] intArray = {1, 2, 3, 4, 5};
        List<Integer> intArrayList = new ArrayList<>();
        for (int num : intArray) {
            intArrayList.add(num);
        }
        System.out.println("Integer ArrayList: " + intArrayList);
    }

    //ArrayList -> Array conversion
    //for string arraylist to array
    private static void arrayListToArray() {
        List<String> arrayList = new ArrayList<>();
        arrayList.add("Dog");
        arrayList.add("Cat");
        arrayList.add("Rabbit");
        String[] array = arrayList.toArray(new String[0]);
        System.out.println("Array: " + Arrays.toString(array));
    }

    //for integer arraylist to array
    private static void intArrayListToArray() {
        List<Integer> intArrayList = new ArrayList<>();
        intArrayList.add(10);
        intArrayList.add(20);
        int[] array = intArrayList.stream().mapToInt(Integer::intValue).toArray();
        System.out.println("Array: " + Arrays.toString(array));
    }

    // Array -> String conversion
    //using String.join for string array to string
    private static void arrayToString() {
        String[] array = {"Hello", "World"};
        String result = String.join(" ", array);
        System.out.println("String: " + result);
    }

    //using StringBuilder for integer array to string
    private static void intArrayToString() {    
        int[] intArray = {1, 2, 3, 4, 5};
        StringBuilder stringBuilder = new StringBuilder();
        for (int num : intArray) {
            stringBuilder.append(num).append(" ");
        }
        String result = stringBuilder.toString().trim();
        System.out.println("String: " + result);
    }

    // String -> Array conversion
    //using String.split for string to string array
    private static void stringToArray() {
        String str = "Java is fun";
        String[] array = str.split(" ");
        System.out.println("Array: " + Arrays.toString(array));
    }

    

}
