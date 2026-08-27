/*
Selection Sort is a comparison-based sorting algorithm. 
It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion 
and swapping it with the first unsorted element.

Find the smallest element and swap it with the first element. This way we get the smallest element 
at its correct position.
Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.

Complexity Analysis of Selection Sort
Time Complexity: O(n2) ,as there are two nested loops:

One loop to select an element of Array one by one = O(n)
Another loop to compare that element with every other Array element = O(n)
Therefore overall complexity = O(n) * O(n) = O(n*n) = O(n2)
Auxiliary Space: O(1) as the only extra memory used is for temporary variables.

Advantages of Selection Sort
Easy to understand and implement, making it ideal for teaching basic sorting concepts.
Requires only a constant O(1) extra memory space.
It requires less number of swaps (or memory writes) compared to many other standard algorithms. 
Only cycle sort beats it in terms of memory writes. Therefore it can be simple algorithm choice when 
memory writes are costly.
Disadvantages of the Selection Sort
Selection sort has a time complexity of O(n^2) makes it slower compared to algorithms like Quick Sort 
or Merge Sort.
Does not maintain the relative order of equal elements which means it is not stable.
Applications of Selection Sort
Perfect for teaching fundamental sorting mechanisms and algorithm design.
Suitable for small lists where the overhead of more complex algorithms isn't justified and memory 
writing is costly as it requires less memory writes compared to other standard sorting algorithms.
Heap Sort algorithm is based on Selection Sort.
Question 1: Is Selection Sort a stable sorting algorithm?

Answer: No, Selection Sort is not stable as it may change the relative order of equal elements.

Question 2: What is the time complexity of Selection Sort?

Answer: Selection Sort has a time complexity of O(n^2) in the best, average, and worst cases.

Question 3: Does Selection Sort require extra memory?

Answer: No, Selection Sort is an in-place sorting algorithm and requires only O(1) additional space.

Question 4: When is it best to use Selection Sort?

Answer: Selection Sort is best used for small datasets, educational purposes, 
or when memory usage needs to be minimal.

Question 5: How does Selection Sort differ from Bubble Sort?

Answer: Selection Sort selects the minimum element and places it in the correct position with fewer swaps, 
while Bubble Sort repeatedly swaps adjacent elements to sort the array.
*/
public class selectsort1 {
    public static void selectsort(int arr[]){
        for(int i=0;i<arr.length-1;i++){
            int minPos=i;
            for(int j=i+1;j<arr.length;j++){
                if(arr[minPos]<arr[j]){ /* for ascending and decending order just condition needed to be changed 
                    for ascending > is used for decending < is used */ 
                    minPos=j;
                }
            }
            // swap 
            int temp=arr[minPos];
            arr[minPos]=arr[i];
            arr[i]=temp;
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
        selectsort(arr);
        printarr(arr);
    }
}    
    

