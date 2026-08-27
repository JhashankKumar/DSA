package Java;
/*
Given two strings s1 and s2 and below operations that can be performed on s1. 
The task is to find the minimum number of edits (operations) to convert 's1' into 's2'.  

Insert: Insert any character before or after any index of s1
Remove: Remove a character of s1
Replace: Replace a character at any index of s1 with some other character.
Note: All of the above operations are of equal cost. 

Examples: 

Input: s1 = "geek", s2 = "gesek"
Output: 1
Explanation: We can convert s1 into s2 by inserting an 's' between two consecutive 'e' in s1.

Input: s1 = "gfg", s2 = "gfg"
Output: 0
Explanation: Both strings are same.

Input: s1 = "abcd", s2 = "bcfe"
Output: 3
Explanation: We can convert s1 into s2 by removing 'a', replacing 'd' with 'f' and inserting 'e' at the end. 
*/
public class EditDistance {
    public static int editDistance(String str1, String str2){
        int n = str1.length();
        int m = str2.length();
        int dp[][] = new int[n+1][m+1];
        //initialize
        for(int i=0;i<n+1;i++){
            for(int j=0;j<m+1;j++){
                if(i==0){
                    dp[i][j] = j;
                }
                if(j==0){
                    dp[i][j] = i;
                }
            }
        }
        //bottom up
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                if(str1.charAt(i-1)==str2.charAt(j-1)){ //same
                    dp[i][j] = dp[i-1][j-1];
                }else{ //differ
                    int add = dp[i][j-1]+1;
                    int del = dp[i-1][j]+1;
                    int rep = dp[i-1][j-1]+1;
                    dp[i][j] = Math.min(add, Math.min(del, rep));
                }
            }
        }
        for(int i=0;i<n+1;i++){
            for(int j=0;j<m+1;j++){
                System.out.print(dp[i][j]+" ");
            }
            System.out.println();
        }
        return dp[n][m];
    }
    public static void main(String[] args) {
        String word1 = "intention";
        String word2 =  "execution";
        System.out.println(editDistance(word1, word2));
    }
    
}
