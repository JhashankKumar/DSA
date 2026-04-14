/*
You are given n pairs of numbers. In every pair, the first number is always smaller than 
the second number. A pair (c, d) can follow another pair (a, b) if b < c. 
Chain of pairs can be formed in this fashion. Find the longest chain which can be formed 
from a given set of pairs.

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, 
then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}
*/
/*
[Approach] Sort the pairs based on the second element and then apply a greedy approach to 
find the longest chain.
Steps to solve the problem:
Sort the pairs in increasing order of their second element.
1. Initialize a variable to keep track of the length of the longest chain (chainlen) and 
set it to 1 (since at least one pair can always form a chain).
2. Initialize a variable (chainEnd) to keep track of the end of the last selected pair, 
and set it to the second element of the first pair.
3. Iterate through the sorted pairs starting from the second pair:
4. If the first element of the current pair is greater than the chainEnd, it means we can extend 
the chain by including this pair. In this case, increment the chainlen and update the chainEnd to 
the second element of the current pair.
5. Continue this process until you have iterated through all the pairs.    
*/
import java.util.*;
public class maxLenChainPair {
    public static void main(String[] args) {
        int pairs[][]={{5,24},{39,60},{5,28},{27,40},{50,90}};

        solveUsingArray(pairs);
        SolveUsingArrayList(pairs);
    }

    public static void solveUsingArray(int pairs[][]){
        //sort the pairs on the basis of their second element in ascending order
        Arrays.sort(pairs,Comparator.comparingDouble(o->o[1]));
        int chainlen=1;
        int chainEnd = pairs[0][1];//last selected pair end // chain end
        System.out.print("("+pairs[0][0]+","+pairs[0][1]+") ");
        for(int i=1;i<pairs.length;i++){
            if(pairs[i][0]>chainEnd){
                chainlen++;
                System.out.print("("+pairs[i][0]+","+pairs[i][1]+") ");
                chainEnd=pairs[i][1];
            }
        }
        System.out.println(chainlen);
    }

    public static void SolveUsingArrayList(int pairs[][]){
        //sort the pairs on the basis of their second element in ascending order
        //sort in arraylist is done by using comparator and lambda function
        List<int[]> pairList = new ArrayList<>();
        for(int[] pair : pairs){
            pairList.add(pair);
        }
        // pairList.sort(Comparator.comparingDouble(o->o[1]));
        Collections.sort(pairList,Comparator.comparingDouble(o->o[1]));
        int chainlen=1;
        int chainEnd = pairList.get(0)[1];//last selected pair end // chain end
        System.out.print("("+pairList.get(0)[0]+","+pairList.get(0)[1]+") ");
        for(int i=1;i<pairList.size();i++){
            if(pairList.get(i)[0]>chainEnd){
                chainlen++;
                System.out.print("("+pairList.get(i)[0]+","+pairList.get(i)[1]+") ");
                chainEnd=pairList.get(i)[1];
            }
        }
        System.out.println(chainlen);
    }
    
}
