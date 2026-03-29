package RecursionBasics;

public class factorial {
    public static int fact(int n){
        if(n==0){
            return 1;
        }
        int f = n*fact(n-1);
        return f;
    }
    public static void main(String[] args) {
        int n=12;
        System.err.println(fact(n));
    }
}
