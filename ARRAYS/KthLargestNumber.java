// Kth largest element in an array
/*
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
 
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

*/
import java.util.PriorityQueue;

public class KthLargestNumber {
    public static void main(String[] args) {
        int arr[] = { 3, 2, 1, 5, 5, 6, 4 };
        int k = 2;
        System.out.println(findKthLargest(arr, k));
    }

    // using priority queue
    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            pq.offer(nums[i]);
        }

        while (!pq.isEmpty() && k > 1) {
            pq.poll();
            k--;
        }

        return pq.isEmpty() ? 0 : pq.peek();

    }
}
