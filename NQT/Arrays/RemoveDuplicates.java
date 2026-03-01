import java.util.*;

public class RemoveDuplicates {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int array_size = scanner.nextInt();
        System.out.println("Enter " + array_size + " integers:");
        int input_array[] = new int[array_size];
        for(int i = 0;i<array_size;i++){
            input_array[i] = scanner.nextInt();
        }
        scanner.close();
        ArrayList<Integer> result = removeDuplicates(input_array);
        System.out.println("Array after removing duplicates:");
        for(int num : result){
            System.out.print(num + " ");
        }
    }
    private static ArrayList<Integer> removeDuplicates(int array[]){
       ArrayList<Integer> uniqueList = new ArrayList<>();
       for(int num : array){
           if(!uniqueList.contains(num)){
               uniqueList.add(num); 
           }
       }
         return uniqueList;
    }
}
