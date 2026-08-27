/*
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent 
elements if they are in the wrong order. This algorithm is not efficient for large data sets as its 
average and worst-case time complexity are quite high.

Sorts the array using multiple passes. After the first pass, the maximum goes to end 
(its correct position). Same way, after second pass, the second largest goes to second last position 
and so on.
In every pass, process only those that have already not moved to correct position. After k passes, 
the largest k must have been moved to the last k positions.
In a pass, we consider remaining elements and compare all adjacent and swap if larger element is 
before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at 
its correct position.

Complexity Analysis of Bubble Sort:
Time Complexity: O(n2)
Auxiliary Space: O(1)
Please refer Complexity Analysis of Bubble Sort for details.


Advantages of Bubble Sort:
Bubble sort is easy to understand and implement.
It does not require any additional memory space.
It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
Disadvantages of Bubble Sort:
Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
Bubble sort has almost no or limited real world applications. It is mostly used in academics to teach different ways of sorting.
*/
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
