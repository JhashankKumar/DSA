package RecursionBasics;
/*time complexity of optimised is O(log n) */
public class optimised_power {
    public static int power(int a,int n){
        if(n==0){
            return 1;
        }
        int halfpow =power(a, n/2);
        int halfpowsq = halfpow * halfpow;
        //if n is odd
        if(n%2!=0){
            halfpowsq = a*halfpowsq;
        }
        return halfpowsq;
    }
    public static void main(String[] args) {
        int a=2;
        int n=5;
        System.out.println(power(a, n));
    }
}
