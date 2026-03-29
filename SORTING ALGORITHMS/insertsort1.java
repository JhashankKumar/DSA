public class insertsort1 {
    public static void insertsort(int arr[]){
        for(int i=1;i<arr.length;i++){
            int current=arr[i];
            int previous=i-1;
            //finding out the correct postion to insert
            while(previous >=0 && arr[previous]>current){ /* for ascending and decending order just condition needed to be changed 
                for ascending > is used for decending < is used  at current */ 
                arr[previous+1]=arr[previous];
                previous--;
            }
            //insertion
            arr[previous+1]=current;
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
        insertsort(arr);
        printarr(arr);
    }
}
   

    
    

