package RecursionBasics;

public class power_recursion {
    public static int power(int x,int n){
        if(n==0){
            return 1;
        }
        else if(x==0){
            return 0;
        }
        else{
            return x*power(x, n-1);
        }
    }
    public static void main(String[] args) {
        System.out.println(power(2, 10));
    }
}