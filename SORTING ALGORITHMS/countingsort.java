//Counting Sort
/*Counting Sort is an efficient sorting algorithm that works by counting the occurrences of each unique element in the input array. It is particularly effective when the range of input values is not significantly larger than the number of elements to be sorted. The algorithm operates in linear time, O(n + k), where n is the number of elements in the input array and k is the range of the input values. Counting Sort is a non-comparison-based sorting algorithm, which means it does not compare elements directly to determine their order. Instead, it uses an auxiliary array to count the occurrences of each unique element and then reconstructs the sorted output based on these counts.
Advantages of Counting Sort:
1. Linear Time Complexity: Counting Sort can achieve a time complexity of O(n + k), making it efficient for sorting integers when the range of input values (k) is not significantly larger than the number of elements (n).
2. Non-Comparison-Based: Counting Sort does not rely on comparisons between elements, which can lead to faster sorting in certain cases, especially when the input values are small integers.
3. Stable Sorting: Counting Sort is a stable sorting algorithm, meaning that it preserves the relative  order of equal elements in the sorted output.
4. Suitable for Specific Data Types: Counting Sort is particularly effective for sorting integers or other discrete data types, making it a good choice for certain applications such as sorting ages, grades, or other categorical data.
Disadvantages of Counting Sort: 
1. Limited to Integer Sorting: Counting Sort is primarily designed for sorting integers and may not be suitable for sorting other data types, such as floating-point numbers or strings.
2. Space Complexity: Counting Sort requires additional space for the count array, which can be significant if the range of input values (k) is large. This can lead to inefficient memory usage in cases where the input values are widely distributed.
3. Not In-Place: Counting Sort is not an in-place sorting algorithm, as it requires additional space for the count array and the output array, which can be a disadvantage in memory-constrained environments.
4. Performance Degradation with Large Range: If the range of input values (k) is significantly larger than the number of elements (n), the performance of Counting Sort can degrade, as it may require a large count array and increased time to process the counts.
Applications of Counting Sort:
1. Sorting Integers: Counting Sort is particularly effective for sorting integers, especially when the range of input values is small compared to the number of elements.
2. Sorting Categorical Data: Counting Sort can be used to sort categorical data, such as grades, ages, or other discrete values, where the range of possible values is limited.
3. Radix Sort: Counting Sort is often used as a subroutine in Radix Sort    to sort individual digits of numbers, making it an essential component of this more complex sorting algorithm.
4. Frequency Counting: Counting Sort can be used to count the frequency of elements in a dataset, which can be useful in various applications such as histogram generation or frequency analysis.
*/
public class countingsort{
    public static void Counting(int arr[]) {
        int largest = Integer.MIN_VALUE;
        for(int i=0;i<arr.length;i++){
            largest = Math.max(largest, arr[i]);
        }
        int count[] = new int[largest+1];
        for(int i=0;i<arr.length;i++){
        count[arr[i]]++;
        }
        //sorting
        int j=0;
        for(int i=0;i<count.length;i++){
        while(count[i]>0){
        arr[j] = i;
        j++;
        count[i]--;
        }
        }
    }
    public static void main(String[] args) {
        int arr[] = {4,5,1,3,2};
        Counting(arr);
    }
}