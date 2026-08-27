package MaxPiramidHeight;
//Find maximum height pyramid from the given array of objects
/*
Given n objects, with each object has width wi. We need to arrange them in a pyramidal way 
such that :

Total width of ith is less than (i + 1)th.
Total number of objects in the ith is less than (i + 1)th.

The task is to find the maximum height that can be achieved from given objects.

Examples :
Input : arr[] = {40, 100, 20, 30}
Output : 2
Top level : 30.
Lower (or bottom) level : 20, 40 and 100
Other possibility can be placing
20 on the top, and at second level any
other 4 objects. Another possibility is
to place 40 at top and other three at the
bottom.

Input : arr[] = {10, 20, 30, 50, 60, 70}
Output : 3

Approach:
The idea is to use greedy approach by placing the object with the lowest width at the top, 
the next object at the level right below and so on. To find the maximum number of levels, 
sort the given array and try to form pyramid from top to bottom. 
Find the smallest element of array i.e first element of array after sorting, place it on the top. 
Then try to build levels below it with greater number of objects and greater width.

Below is the implementation of this approach:

*/
import java.util.*;
public class MaxPiramidHeight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        int arr[] = new int[length];
        for(int i=0;i<length;i++){
            arr[i] = sc.nextInt();
        }
        int height = maxPiramidHight(arr, length);
        System.out.print(height);

    }
    public static int maxPiramidHight(int[] width, int length){
        Arrays.sort(width);
        int prev_width = width[0];
        int prev_count = 1;
        int curr_width = 0;
        int curr_count = 0;
        int ans = 0;
        for(int i=1;i<length;i++){
            curr_width += width[i];
            curr_count += 1;

            if(curr_count > prev_count && curr_width > prev_width){

                prev_count = curr_count;
                prev_width = curr_width;

                curr_count = 0;
                curr_width = 0;

                ans++;
            }
        }
        return ans; 
    }
}
