public class fibonacci {
    //recursion
    public static int fibRec(int n ){
        if(n==0||n==1){
            return n;
        }
        return fibRec(n-1)+fibRec(n-2);
    }
    //memoization 
    public static int fibMemo(int n, int dp[]){
        if(n==0||n==1){
            return n;
        }
        if(dp[n] != 0){ // fib[n] already calculated
            return dp[n];
        }
        dp[n] = fibMemo(n-1, dp)+fibMemo(n-2, dp);
        return dp[n];
    }
    //tabulation
    public static int fibTabu(int n){
        int dp[] = new int[n+1];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2;i<=n;i++){
            dp[i] = dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
    public static void main(String[] args) {
        int n = 5;
        int dp[] = new int[n+1];
        System.out.println(fibMemo(n, dp));
        System.out.println(fibTabu(n));
        System.out.println(fibRec(n));
    }
}