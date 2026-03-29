import java.util.Arrays;

public class climbingStairs {
    //recursion
    public static int countWaysRec(int n){
        if(n==0){
            return 1;
        }
        if(n<0){
            return 0;
        }
        return countWaysRec(n-1)+countWaysRec(n-2);
    }
    //memoization
    public static int countWaysMemo(int n, int Ways[]){
        if(n==0){
            return 1;
        }
        if(n<0){
            return 0;
        }
        if(Ways[n] != -1){ //already calculated
            return Ways[n];
        }
        Ways[n] =  countWaysMemo(n-1, Ways)+countWaysMemo(n-2, Ways);
        return Ways[n];
    }
    //tabulation
    public static int countWaysTabu(int n){
        int dp[] = new int[n+1];
        dp[0] = 1;
        for(int i=1;i<=n;i++){
            if(i==1){
                dp[i] = dp[i-1]+0;
            }
            else{
                dp[i] = dp[i-1]+dp[i-2];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 5;
        int ways[] = new int[n+1];
        Arrays.fill(ways,-1);
        System.out.println(countWaysRec(n));
        System.out.println(countWaysMemo(n, ways));
        System.out.println(countWaysTabu(n));
    }
}
