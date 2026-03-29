package Divide_and_Conquer;
public class MergeSort {
    public static void printarr(int arr[]){ // it will print sortted array
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void mergesort(int arr[],int si, int ei){
       if(si==ei){
        return;
       } 
       //this part of code will divide the array
       int mid = si+(ei-si)/2;//mid part division
       mergesort(arr, si,mid); //left part 
       mergesort(arr, mid+1, ei);//right part
       merge(arr,si,mid,ei);
    }   
    //this part of array will merge the array in a sequence in a temporary array
    public static void merge(int arr[],int si, int mid,int ei){
        /*for a seven element array mid left(0,3)=4 and right(4,6)=3 */
        int temp[]=new int[ei-si+1];
        int i = si;//iterator for left part
        int j = mid+1;//iterator for right part
        int k = 0; //iterator for temp arr
        while(i<=mid&&j<=ei){//merge sort of two small sub sorted array in temp array
            if(arr[i]<arr[j]){ //in this if condition ascending and decending order will be decided
                temp[k]=arr[i];
                i++;
            }
            else{
                temp[k]=arr[j];
                j++;
            }
            k++;
        }
        //after merging all sorted elements sometimes single elements will be left over those are merged using below code
        //left part
        while(i<=mid){
            temp[k++]=arr[i++];
        }
        //right part
        while(j<=ei){
            temp[k++]=arr[j++];
        }
        //copy temp array to original array
        for(k=0,i=si;k<temp.length;k++,i++){
            arr[i]= temp[k];
        }
    }
    public static void main(String[] args) {
        int arr[]={6,3,9,5,2,8};
        mergesort(arr, 0, arr.length-1);
        printarr(arr);
    }
}
