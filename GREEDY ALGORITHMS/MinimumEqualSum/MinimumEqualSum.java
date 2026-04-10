package MinimumEqualSum;

import java.util.Scanner;

//Maximum equal sum of three stacks
/*
The three stacks s1, s2 and s3, each containing positive integers, are given. 
The task is to find the maximum possible equal sum that can be achieved by removing elements 
from the top of the stacks. Elements can be removed from the top of each stack, 
but the final sum of the remaining elements in all three stacks must be the same. 
The goal is to determine the maximum possible equal sum that can be achieved after removing elements.

Note: The stacks are represented as arrays, where the first index of the array 
corresponds to the top element of the stack.

Examples: 

Input: s1 = [3, 2, 1, 1, 1], s2 = [4, 3, 2], s3 = [2, 5, 4, 1]
Output: 5
Explanation: We can pop 2 elements from the 1st stack, 1 element from the 2nd stack and 
2 elements from the 3rd stack.

 
Input: s1 = [3, 10]
       s2 = [4, 5]
       s3 = [2, 1]
Output: 0
Explanation: Sum can only be equal after removing all elements from all stacks.
*/
/*
Greedy Approach - O(n1 + n2 + n3) Time and O(1) Space
The idea is to compare the sum of each stack, if they are not same, remove the top element of 
the stack having the maximum sum.

Algorithm for solving this problem: 

Find the sum of all elements of in individual stacks.
If the sum of all three stacks is the same, then this is the maximum sum.
Else remove the top element of the stack having the maximum sum among three of stacks. 
Repeat step 1 and step 2.
The approach works because elements are positive. To make sum equal, we must remove some 
element from stack having more sum, and we can only remove from the top.
*/

import java.util.*;
public class MinimumEqualSum {
    public static void main(String[] args) {
        //using ArrayList to represent stack 
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        ArrayList<Integer> s1 = new ArrayList<>();
        ArrayList<Integer> s2 = new ArrayList<>();
        ArrayList<Integer> s3 = new ArrayList<>();
        for(int i = 0; i < n1; i++){
            s1.add(sc.nextInt());   
        }
        for(int i = 0; i < n2; i++){
            s2.add(sc.nextInt());   
        }
        for(int i = 0; i < n3; i++){
            s3.add(sc.nextInt());   
        }

    }

    public static int maxEqualSum(ArrayList<Integer> s1, ArrayList<Integer> s2, ArrayList<Integer> s3){
        int sum1 = 0, sum2 = 0, sum3 = 0;
        for(int i : s1){
            sum1 += i;
        }
        for(int i : s2){
            sum2 += i;
        }
        for(int i : s3){
            sum3 += i;
        }

        while(true){
            if(s1.size() == 0 || s2.size() == 0 || s3.size() == 0){
                return 0;
            }
            if(sum1 == sum2 && sum2 == sum3){
                return sum1;
            }
            if(sum1 >= sum2 && sum1 >= sum3){
                sum1 -= s1.get(0);
                s1.remove(0);
            } else if(sum2 >= sum1 && sum2 >= sum3){
                sum2 -= s2.get(0);
                s2.remove(0);
            } else {
                sum3 -= s3.get(0);
                s3.remove(0);
            }
        }
    }
}
