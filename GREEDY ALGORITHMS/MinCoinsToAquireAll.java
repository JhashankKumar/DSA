//Minimum cost for acquiring all coins with k extra coins allowed with every coin
/*
You are given a list of N coins of different denominations. 
You can pay an amount equivalent to any 1 coin and can acquire that coin. In addition, 
once you have paid for a coin, we can choose at most K more coins and can acquire those for free. 
The task is to find the minimum amount required to acquire all the N coins for a given value of K.

Examples : 

Input : coin[] = {100, 20, 50, 10, 2, 5}, 
        k = 3
Output : 7

Input : coin[] = {1, 2, 5, 10, 20, 50}, 
        k = 3
Output : 3

As per the question, we can see that at a cost of 1 coin, we can acquire at most K+1 coins. 
Therefore, in order to acquire all the n coins, we will be choosing ceil(n/(k+1)) coins and the cost 
of choosing coins will be minimum if we choose the smallest ceil(n/(k+1)) ( Greedy approach). 
The smallest ceil(n/(k+1)) coins can be found by simply sorting all the N values in increasing order. 
If we should check for time complexity (n log n) is for sorting element and (k) is for adding the 
total amount. So, finally Time Complexity: O(n log n). 
*/

import java.util.*;
public class MinCoinsToAquireAll {
    public static void main(String[] args){
        Scanner sc = Scanner(System.in);
        int length = sc.nextInt();
        int coins[] = new int[length];
        int k = sc.nextInt();
        int cost = minRequiredCost(coins, k, length);

    }
    public static int minRequiredCost(int coins[], int k, int length){
        int minCoinsRequired = (int) Math.ceil(length/(k+1));
        int cost =  cost(coins, minCoinsRequired);
        return cost;

    }
    public static int cost(int[] coins, int count) {
        Arrays.sort(coins);
        int cost = 0;
        for(int i=0;i<count;i++){
            cost += coins[i];
        }
        return cost;
    }
}
