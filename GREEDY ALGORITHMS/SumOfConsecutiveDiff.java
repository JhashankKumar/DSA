// Maximize sum of consecutive differences in a circular array
/*
Given an array of n elements. Consider array as circular array i.e element after an is a1. 
The task is to find maximum sum of the difference between consecutive elements with rearrangement 
of array element allowed i.e after rearrangement of element find 
|a1 - a2| + |a2 - a3| + ...... + |an - 1 - an| + |an - a1|. 

Examples: 

Input : arr[] = { 4, 2, 1, 8 }
Output : 18
Rearrange given array as : { 1, 8, 2, 4 }
Sum of difference between consecutive element
= |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1|
= 7 + 6 + 2 + 3
= 18.

Input : arr[] = { 10, 12, 15 }
Output : 10
The idea is to use Greedy Approach and try to bring elements having greater difference closer. 
Consider the sorted permutation of the given array a1, a1, a2,...., an - 1, 
an such that a1 < a2 < a3.... < an - 1 < an. 
Now, to obtain the answer having maximum sum of difference between consecutive element, 
arrange element in following manner: 
a1, an, a2, an-1,...., an/2, a(n/2) + 1 
We can observe that the arrangement produces the optimal answer, as all a1, a2, a3,....., a(n/2)-1, 
an/2 are subtracted twice while a(n/2)+1 , a(n/2)+2, a(n/2)+3,....., an - 1, an are added twice. 

Note:  a(n/2)+1 This term is considered only for even n because for odd n, 
it is added once and subtracted once and hence cancels out. 

Implementation:

*/

import java.util.Arrays;

public class SumOfConsecutiveDiff {
    public static long maxSum(Long[] arr) {
        Arrays.sort(arr);

        long[] sorted = new long[arr.length];
        int left = 0;
        int right = arr.length - 1;
        int index = 0;

        while (left <= right) {
            if (left != right) {
                sorted[index++] = arr[left++];
                sorted[index++] = arr[right--];
            } else {
                sorted[index++] = arr[left++];
            }
        }

        long sum = 0;
        for (int i = 0; i < sorted.length - 1; i++) {
            sum += Math.abs(sorted[i] - sorted[i + 1]);
        }

        sum += Math.abs(sorted[0] - sorted[sorted.length - 1]);

        return sum;
    }

    public static void main(String[] args) {
        Long[] arr = {4L, 2L, 1L, 8L};
        System.out.println(maxSum(arr)); // Output: 18
    }
    
}