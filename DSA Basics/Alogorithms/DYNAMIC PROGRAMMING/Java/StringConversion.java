package Java;
public class StringConversion {
    public static int LCS(String str1, String str2){
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

    public static void conversion(String str1, String str2){
        int ans = LCS(str1,str2);
        int n = str1.length();
        int m = str2.length();
        int del = n-ans;
        int add = m-ans;
        System.out.println("delete operations = "+del);
        System.out.println("add operations = "+add);

    }
    public static void main(String[] args) {
        String str1 = "pear";
        String str2 = "sea";
        conversion(str1, str2);
    }
}
