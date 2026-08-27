package RecursionBasics;

public class increment {
    public static void printinc(int n){
        if(n==10){ // base case 
            System.out.println(n);
            return;
        }
        System.out.print(n+" ");
        printinc(n+1);  // calling a function itself
    }
    public static void main(String[] args) {
        int n = 1;
        printinc(n);
    }
    
}
