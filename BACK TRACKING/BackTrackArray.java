public class BackTrackArray {
    public static void changeArr(int arr[],int i,int val){
        //base case
        if(i==arr.length){
            printarr(arr); //it prints forward call array
            return;
        }
        //recursion
        arr[i] = val;
        changeArr(arr, i+1, val+1); //forward call step
        arr[i] = arr[i]-2;//backtracking step
    }
    public static void printarr(int arr[]){ // prints an array
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int arr[]=new int[5];
        changeArr(arr, 0, 1);
        printarr(arr);//it prints backtracking array
    }
    
}
