import java.util.*;
class practice{
    public static void main(String[] args) {
       
        System.out.println("Test your code here!\n");

        // Get a result of your code

        System.out.println(max());
    }
    public static int max() {
        int maxval = Integer.MIN_VALUE;
        Scanner sc = new Scanner(System.in);
        // Put your code here
        int number = sc.nextInt();
        while(number!=0){
            maxval = Math.max(maxval,number);
            number = sc.nextInt();
        }
        return maxval;
    }
}        