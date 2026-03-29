package Divide_and_Conquer;
//modified binary search used for search in rotated sorted array
public class ModifiedBinarySearch {
    public static int search(int arr[],int tar,int si,int ei){
        //base case
        if(si>ei){
            return -1;
        }
        //frist finding mid
        int mid = si+(ei-si)/2;
        //checking value at mid=target
        if(arr[mid]==tar){
            return mid;
        }
        //mid lie on L1
        if(arr[si]<=arr[mid]){
            //case a: left search
            if(arr[si]<=tar && tar<=arr[mid]){
                return search(arr, tar, si,mid);
            } 
            else{
                // case b: right search
                return search(arr, tar, mid+1, ei);
            }   
        }
        //mid lie on L2
        else{
            // case c: right search
            if(arr[mid]<=tar && tar<=arr[ei]){
                return search(arr, tar, mid+1, ei);
            }
            //case d: left search
            else{
                return  search(arr, tar, si, mid-1);
            }
        }
        

    }
    public static void main(String[] args) {
        int arr[]={4,5,6,7,0,1,2};
        int target=0;
        int tarIdx = search(arr,target , 0, arr.length-1);
        System.out.println(tarIdx);
    }
    
}
