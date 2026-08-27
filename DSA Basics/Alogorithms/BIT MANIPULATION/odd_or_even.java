import java.util.Scanner;

public class odd_or_even {
    private static boolean b;
    public static void oddoreven(int n){
        int bitmask=1;
        b = (n & bitmask) == 0;
        if(b){
            System.out.println("even number");
        }
        else{
            System.out.println("odd number");
        }
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            oddoreven(n);
        }

        
    }
    
}
