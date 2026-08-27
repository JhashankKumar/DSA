package Java;
//Longest Common Subsequence(LCS)
/*
Given two strings, s1 and s2, find the length of the Longest Common Subsequence. 
If there is no common subsequence, return 0. A subsequence is a string generated from the original 
string by deleting 0 or more characters, without changing the relative order of the remaining characters.

For example, subsequences of "ABC" are "", "A", "B", "C", "AB", "AC", "BC" and "ABC". In general, 
a string of length n has 2n subsequences.

Examples:

Input: s1 = "ABC", s2 = "ACD"
Output: 2
Explanation: The longest subsequence which is present in both strings is "AC".

Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
Explanation: The longest common subsequence is "GTAB".

Input: s1 = "ABC", s2 = "CBA"
Output: 1
Explanation: There are three longest common subsequences of length 1, "A", "B" and "C".
*/
public class LongestCS{
    //recursion
    public static int lcs(String str1, String str2, int n, int m){
        if(n==0||m==0){
            return 0;
        }
        if(str1.charAt(n-1)==str2.charAt(m-1)){
            return lcs(str1, str2, n-1, m-1)+1;
        }
        else{
            int ans1 = lcs(str1, str2, n-1, m);
            int ans2 = lcs(str1, str2, n, m-1);
            return Math.max(ans1, ans2);
        }
    }
    //memoization
    public static int lcsMemo(String str1, String str2, int n, int m, int dp[][]){
        if(n==0||m==0){
            return 0;
        }
        if(dp[n][m] != -1){
            return dp[n][m];
        }
        if(str1.charAt(n-1)==str2.charAt(m-1)){
            dp[n][m] =  lcsMemo(str1, str2, n-1, m-1,dp)+1;
            return dp[n][m];
        }
        else{
            int ans1 = lcsMemo(str1, str2, n-1, m, dp);
            int ans2 = lcsMemo(str1, str2, n, m-1,dp);
            return dp[n][m]= Math.max(ans1, ans2);
        }
    }
    //tabulation
    public static int lcsTab(String str1, String str2){
        int n = str1.length();
        int m = str2.length();
        //when array is created in java by default values in cells are initialized with 0
        int dp[][] = new int[n+1][m+1];
        for(int i=1;i<n+1;i++){
            for(int j=1;j<m+1;j++){
                if(str1.charAt(i-1)==str2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
                else{
                    int ans1 = dp[i-1][j];
                    int ans2 = dp[i][j-1];
                    dp[i][j] = Math.max(ans1, ans2);
                }
            }    
        }
        return dp[n][m];
    }
    public static void main(String[] args) {
        String str1 = "abcdge";
        String str2 = "abedg";
        int n = str1.length();
        int m = str2.length();
        int dp[][] = new int[n+1][m+1];
        //initialization
        for(int i=0;i<n+1;i++){
            for(int j=0;j<m+1;j++){
                dp[i][j] = -1;
            }
        }
        System.out.println(lcs(str1, str2, str1.length(), str2.length()));
        System.out.println(lcsMemo(str1, str2, n, m, dp));
        System.out.println(lcsTab(str1, str2));
    }
    
}
