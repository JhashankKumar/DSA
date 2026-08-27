

import java.util.Stack;

public class NextGreater {
    public static void main(String[] args) {
        int arr[] = {6, 8, 0, 1, 3};
        Stack<Integer> s = new Stack<>();
        int nexGreater[] = new int[arr.length];
        //there are different forms of the question in nextGreater
        //if nextGreater for an element in left for loop is below
        //for(int i = 0;i<=arr.length-1;i++)
        //with this for loop change in code we obtain nextGreater left
        //if nextGreater for an element in right for loop is below
        for(int i=arr.length-1;i>=0;i--){
            //with this for loop change in code we obtain nextGreater right
            //step 1: while loop
            //NOTE: in stack index of value is stored 
            //condition 1: stack is empty or not [true when is not empty]
            //condition 2: value in stack <= value in array [true]
            while(!s.empty()&&s.peek()<= arr[i]){
                s.pop();
            }
            //step 2: if-else 
            //stack is empty or not checking[empty = true]loop will execute
            //in nextGreater array -1 is stored
            if(s.empty()){
                nexGreater[i] = -1;
            }
            //in else value in stack is stored in nextGreater as value in index[i] array is smaller than value in index[i-1]
            else{
                nexGreater[i] = s.peek();
            }
            //step 3: push in s stack
            //here element is not pushed only its index value is pushed
            s.push(arr[i]);
        }
        for(int i=0;i<=nexGreater.length-1;i++){
            System.out.print(nexGreater[i]+" ");
        }
        System.out.println();
    }
    
}
