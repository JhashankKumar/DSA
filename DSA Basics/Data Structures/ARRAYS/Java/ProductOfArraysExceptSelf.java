package Java;
// Product of Array Except Self
/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
 
*/
public class ProductOfArraysExceptSelf {
    public static void main(String[] args) {
        int arr[] = { 4, 2, 6, 3, 2, 5 };
        int ans[] = productExceptSelfUsingSingleArray(arr);
        int ans2[] = productExceptSelfUsingTwoArray(arr);
        for (int i = 0; i < ans2.length; i++) {
            System.out.print(ans2[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < ans.length; i++) {
            System.out.print(ans[i] + " ");
        }
    }

    public static int[] productExceptSelfUsingSingleArray(int nums[]) {
        //using left and right product array
        int n = nums.length;
        int ans[] = new int[n];
        // calculate left product

        ans[0] = 1;
        for (int i = 1; i < n; i++) {
            ans[i] = ans[i - 1] * nums[i - 1];
        }
        // calculate right product and final answer
        int rightproduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = ans[i] * rightproduct;
            rightproduct *= nums[i];
        }
        return ans;
    }

    public static int[] productExceptSelfUsingTwoArray(int nums[]) {
        // using left and right product array
        int n = nums.length;
        int leftproduct[] = new int[n];
        int rightproduct[] = new int[n];
        int ans[] = new int[n];
        // calculate left product
        leftproduct[0] = 1;
        for (int i = 1; i < n; i++) {
            leftproduct[i] = leftproduct[i - 1] * nums[i - 1];
        }
        // calculate right product
        rightproduct[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            rightproduct[i] = rightproduct[i + 1] * nums[i + 1];
        }
        // calculate final answer
        for (int i = 0; i < n; i++) {
            ans[i] = leftproduct[i] * rightproduct[i];
        }
        return ans;
    }   
}
