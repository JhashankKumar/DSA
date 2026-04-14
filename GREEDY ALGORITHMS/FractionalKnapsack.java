/*
Given two arrays, val[] and wt[], representing the values and weights of item respectively, 
and an integer capacity representing the maximum weight a knapsack can hold, we have to 
determine the maximum total value that can be achieved by putting the items in the knapsack 
without exceeding its capacity.
Items can also be taken in fractional parts if required.

Examples:

Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
Output: 240 
Explanation: We will take the items of weight 10kg and 20kg and 2/3 fraction of 30kg. 
Hence total value will be 60 + 100 + (2/3) * 120 = 240.

Input: val[] = [500], wt[] = [30], capacity = 10
Output: 166.667
*/

/*
Why naive approach will fail?
Case 1: Picking the items with smaller weights first
Example: val[] = [10, 10, 10, 100], wt[] = [10, 10, 10, 30], capacity = 30

If we start picking smaller weights, we can pick the three items of weight 10 → total value = 10+10+10 = 30.
But the optimal choice is to take the last item (value 100, weight 30) → total value = 100.
So, choosing smaller weights first fails here.

Case 2: Picking items with larger value first
Example: val[]= [10, 10, 10, 20], wt[] = [10, 10, 10, 30], capacity = 30

If we start picking higher values, we might choose the last item (value 20, weight 30) → total value = 20.
But the better choice is to take the three items of weight 10 each → total value = 10+10+10 = 30.
So, choosing higher values first also fails.

[Approach] Selecting Items by value/weight Ratio - O(nlogn) Time and O(n) Space
The idea is to always pick items greedily based on their value-to-weight ratio. 
Take the item with the highest ratio first, then the next highest, and so on, until the knapsack is full. 
If any item doesn’t fully fit, then take its fractional part according to the remaining capacity.

Steps to solve the problem:

Calculate the ratio (value/weight) for each item.
Sort all the items in decreasing order of the ratio.
Iterate through items:
if the current item fully fits, add its full value and decrease capacity otherwise, 
take the fractional part that fits and add proportional value.
Stop once the capacity becomes zero.

*/
import java.util.*;
public class FractionalKnapsack {
    public static void main(String[] args) {
        int val[]={60, 100, 120};
        int weight[]={10, 20, 30};
        int w=50;
        //this 2-D array is for ratio storing
        double ratio[][]= new double[val.length][2];
        //0th col => idx ;1st col => ratio
        for(int i=0;i<ratio.length;i++){
            ratio[i][0]=i;
            ratio[i][1]= val[i]/(double)weight[i];
        }
        //ascending order lambda function
        //sorted on bases of ratios values in ascending
        Arrays.sort(ratio,Comparator.comparingDouble(o->o[1]));

        //but we need decending order values so for loop is runned from last idx to frist idx
        int capacity = w;
        int finalValue= 0;
        for(int i=ratio.length-1;i>=0;i--){
            int idx = (int)ratio[i][0];
            if(capacity>=weight[idx]){//include full item
                finalValue += val[idx];
                capacity -= weight[idx];
            }else{
                //include fractional item
                finalValue += (ratio[i][1]*capacity);
                capacity=0;
                break;
            }
        }
        System.out.println(finalValue);
    }  
}
