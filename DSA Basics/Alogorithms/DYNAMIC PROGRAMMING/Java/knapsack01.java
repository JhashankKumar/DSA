package Java;
// 0-1 Knapsack Problem
/*
Given two arrays, val[] and wt[], where each element represents the value and weight of an item 
respectively, also given an integer W representing the maximum capacity of the knapsack 
(the total weight it can hold).Put the items into the knapsack such that the sum of values associated 
with them is the maximum possible, without exceeding the capacity W.

Note: We can either include an item completely or exclude it entirely - we cannot include a fraction 
of an item.

Examples:

Input:  W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
Output: 3
Explanation: There are two items with weight less than or equal to 4. If we select the item with weight 
4, the possible value is 1, and if we select the item with weight 1, the possible value is 3. Hence, 
the maximum possible value is 3. We cannot put both items with weights 4 and 1 together because the 
capacity of the bag is 4.

Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
Output: 0 
Explanation: All the item weights are greater than the knapsack capacity.
*/
public class knapsack01 {
    //recursion
    public static int knapsack_rec(int val[], int wt[], int W, int n){
        if(W == 0 || n==0){
            return 0;
        }
        //item checking is from last 
        if(wt[n-1]<=W){//valid
            //include
            int ans1 = val[n-1]+knapsack_rec(val, wt, W-wt[n-1], n-1);
            //exclude
            int ans2 = knapsack_rec(val, wt, W, n-1);
            return Math.max(ans1, ans2);
        }
        else{ // not valid
            return knapsack_rec(val, wt, W, n-1);
        }
    }
    //memoization
    public static int knapsack_mem(int val[], int wt[], int W, int n, int dp[][]){
        if(W == 0 || n==0){
            return 0;
        }
        if(dp[n][W] != -1){
            return dp[n][W];
        }
        //item checking is from last 
        if(wt[n-1]<=W){//valid
            //include
            int ans1 = val[n-1]+knapsack_mem(val, wt, W-wt[n-1], n-1, dp);
            //exclude
            int ans2 = knapsack_mem(val, wt, W, n-1, dp);
            dp[n][W] =  Math.max(ans1, ans2);
            return dp[n][W];
        }
        else{ // not valid
            dp[n][W] =  knapsack_rec(val, wt, W, n-1);
            return dp[n][W];
        }
    }
    //tabulation
    public static int knapsack_tabu(int val[], int wt[], int W){
        int n = val.length;
        int dp[][] = new int[n+1][W+1];
        for(int i=0;i<dp.length;i++){ // 0th col
            dp[i][0] = 0;
        }
        for(int j=0;j<dp[0].length;j++){ // 0th row
            dp[0][j] = 0;
        }
        for(int i=1;i<n+1;i++){
            for(int j=1;j<W+1;j++){
                int v = val[i-1];//ith item val
                int w = wt[i-1];//ith item wt
                if(w<=j){ // valid
                    int include_profit = v+dp[i-1][j-w];
                    int exclude_profit = dp[i-1][j];
                    dp[i][j] = Math.max(include_profit, exclude_profit);
                }
                else{//invalid
                    int exclude_profit = dp[i-1][j];
                    dp[i][j] = exclude_profit;
                }
            }
        }
        return dp[n][W];
    }
    

    
    public static void main(String[] args) {
        int val[] = {15, 14, 10, 45, 30};
        int wt[] = {2, 5, 1, 3, 4};
        int W =7;
        int dp[][] = new int[val.length+1][W+1];
        for(int i=0;i<dp.length;i++){
            for(int j=0;j<dp[0].length;j++){
                dp[i][j] = -1;
            }
        }
        System.out.println(knapsack_rec(val, wt, W, val.length));
        System.out.println(knapsack_mem(val, wt, W, val.length, dp));
        System.out.println(knapsack_tabu(val, wt, W));
    }
}
