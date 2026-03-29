public class bubblesort1 {
    public static void bubblesort(int arr[]){
        for(int turn=0;turn<arr.length-1;turn++){ //it gives how many numbers are in a array
            for(int j=0;j<arr.length-1;j++){ // it used for sorting a in its original position
                if(arr[j]>arr[j+1]){ // compares for greater number
                    //swap 
                    int temp = arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]= temp;
                }
            }
        }
    }
    public static void printarr(int arr[]){
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int arr[]={5,4,1,3,2};
        bubblesort(arr);
        printarr(arr);
    }
}
