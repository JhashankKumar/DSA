package RecursionBasics;
// checking array is sorted or not
public class array_sort_check {
    public static boolean issorted(int arr[],int i){ // function call 
        if(i==arr.length-1){ // checking length of array is came to end or not
            return true;
        }
        if(arr[i]<arr[i+1]){ /*condition where ascending sort or decending sort is checked */
            /*if "<"symbol is used ascending sort check ">"symbol is used decending sort check */
            return false;
        }
        return issorted(arr,i+1);
    }
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        System.out.println(issorted(arr, 0)); 

    }
    
}
