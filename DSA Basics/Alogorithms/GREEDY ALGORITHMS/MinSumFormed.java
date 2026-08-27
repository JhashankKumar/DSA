//Minimum sum of two numbers formed from digits of an array
/*
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits 
of the array. All digits of given array must be used to form the two numbers.

Examples: 
Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: 604
Explanation: The minimum sum is formed by numbers 358 and 246

Input: arr[] = [5, 3, 0, 7, 4]
Output: 82
Explanation: The minimum sum is formed by numbers 35 and 047 
*/
import java.util.*;

public class MinSumFormed {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        int n = sc.nextInt();
        for(int i=0;i<n;i++){
            arr.add(sc.nextInt());
        }
        // while(sc.hasNextInt()){
        //     arr.add(sc.nextInt());
        // }
        sc.close();
        minSum(arr);
    }
    public static void minSum(ArrayList<Integer> arr){
        Collections.sort(arr);
        String num1 = "";
        String num2 = "";
        for(int i=0;i<arr.size();i++){
            if(i%2==0){
                num1+=arr.get(i);
            }else{
                num2+=arr.get(i);
            }
        }
        int sum = Integer.parseInt(num1)+Integer.parseInt(num2);
        System.out.println(sum);
    }
}
