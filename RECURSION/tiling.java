public class tiling {
    public static int waycount(int n ){//2 x n (floor size)
    //base case
    if(n == 0||n==1){
        return 1;
    }
    //work
    //vertical choice
    int fnm1 = waycount(n-1);
    //horizontal choice
    int fnm2 = waycount(n-2);
    int totalways=fnm1+fnm2;
    return totalways;
   }
   public static void main(String[] args) {
    System.out.println(waycount(4));
   }

}
