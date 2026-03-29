package RecursionBasics;
/*here last occurance of a number is checking and index of last occurance is returned */
public class last_occurance {
    public static int lastOccur(int arr[],int key,int i){
        if(i==arr.length){
            return -1;
        }
        int isfound = lastOccur(arr, key, i+1);
        if(isfound == -1 && arr[i]==key){
            return i;
        }
        return isfound;
    }
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,2,3,1};
        System.out.println(lastOccur(arr, 3, 0));
    }
    
}
