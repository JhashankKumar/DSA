// Longest Increasing Subsequence(LIS)
/*
Given an array arr[] of size n, find the length of the Longest Increasing Subsequence (LIS) i.e., 
the longest possible subsequence in which the elements of the subsequence are sorted in strictly 
increasing order.

Examples:

Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = [30, 20, 10]
Output:1
Explanation: The longest increasing subsequences are [30], [20] and [10]

Input: arr[] = [2, 2, 2]
Output: 1
Explanation:  We consider only strictly increasing subsequences, therefore the longest increasing 
subsequence is [2].

Input: arr[] = [3, 4, 5, 1, 2, 3, 4]
Output: 4
Explanation: The longest strictly increasing subsequence is [1, 2, 3, 4], which gives a maximum length 
of 4. (Note: [3, 4, 5] is also an increasing subsequence, but its length is only 3).
*/

import java.util.*;

public class LongestIS {
    public static int LCS(int arr1[], int arr2[]){
        int n = arr1.length;
        int m = arr2.length;
        int dp[][] = new int[n+1][m+1];
        for(int i=0;i<n+1;i++){
            for(int j=0;j<m+1;j++){
               System.out.print(dp[i][j]+" ");
            }
            System.out.println();
        }
        
        //initialization 
        //in java by default arrays are initialized with zeros
        for(int i=0;i<n+1;i++){
            dp[i][0] = 0;
        }
        for(int j=0;j<m+1;j++){
            dp[0][j] = 0;
        }
    
        //bottom up fill
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                if(arr1[i-1]==arr2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
                else{
                    int ans1 = dp[i-1][j];
                    int ans2 = dp[i][j-1];
                    dp[i][j] = Math.max(ans1,ans2);
                }
            }
        }
        return dp[n][m];
    }
    public static int LIS(int arr[]){
        HashSet<Integer> set = new HashSet<>();
        for(int i=0;i<arr.length;i++){
            set.add(arr[i]);
        }
        int arr2[] = new int[set.size()]; //sorted unique elements
        int i=0;
        for (int num : set) {
            arr2[i] = num;
            i++;
        }
        Arrays.sort(arr2); //ascending order sorted 
        return LCS(arr, arr2);
    }
    public static void main(String[] args) {
        int arr[] = {50,3,10,7,40,80};
        System.out.println(LIS(arr));
    }
    
}
