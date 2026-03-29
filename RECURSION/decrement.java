package RecursionBasics;

public class decrement {
    public static void printDec(int n){
        if(n==1){ // base case 
            System.out.println(n);
            return;
        }
        System.out.print(n+" ");
        printDec(n-1);  // calling a function itself
    }
    public static void main(String[] args) {
        int n = 10;
        printDec(n);
    }
}
