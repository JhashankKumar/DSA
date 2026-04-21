/*
The "Data Doubler" Algorithm:
Imagine you are working as an intern at a music streaming company. You Doss wants to create a new 
'Loop Mode' feature. When a user creates a playlist, the system needs to automatically generate a 
queue that plays th entire playlist once, and then immediately plays the exact same playlist again 
from the start.
Write a program that takes any list of songs (represented by ID numbers) and returns a new list that 
plays the sequence twice back-to-back.
*/
/*
Test cases:

Test Case 1 (Standard):
Input: N = 3 Array = {1, 2, 3}
Expected Output: {1, 2, 3, 1, 2, 3}

Test Case 2 (Single Element):
Input: N = 1 Array = {9}
Expected Output: {9, 9}
*/
public class DataDoubler {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int[] newArr = new int[arr.length*2];
        for(int i = 0;i<arr.length;i++){
            newArr[i] = arr[i];
            newArr[i+arr.length] = arr[i];
        }
        for(int i = 0;i<newArr.length;i++){
            System.out.print(newArr[i]+" ");
        }
        System.out.println();
    }
}
