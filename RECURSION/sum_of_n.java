package RecursionBasics;

public class sum_of_n {
    public static int calcSum(int n){
        if(n==1){ // checking wether n reached 1 or not
            return 1;
        }
        int sn = n + calcSum(n-1);  //function call [recursive call]
        return sn;
      
    }
    public static void main(String[] args) {
        int n = 5;
        System.out.println(calcSum(n)); //function call
    }
    
}
