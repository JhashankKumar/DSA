package RecursionBasics;
//printing possible binary strings of size n without consecutive one's
public class PossibleBinaryStrings {
    public static void PrintBinaryString(int n,int lastplace,String str){
    if(n==0){ //count check of size
        System.out.println(str);
        return;
    }
    //to do work
    /*checking the left most bit if it was zero  next recursion starts and goes till n=0
     * at n=0 it prints "000" as output and then comes to n=1
    */
    PrintBinaryString(n-1,0, str+"0");
    /*at here lastplace = 2 it also 0 then last statements in if condition executes and "001" 
     * like this loop continues and prints all strings except consecutive one strings
     */
    if(lastplace == 0){
        PrintBinaryString(n-1,1, str+1);
    }
    }
    public static void main(String[] args) {
        PrintBinaryString(3, 0, "");
    }
}
    
