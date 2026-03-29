import java.util.Stack;

public class ReverseStack {
    public static void PushAtBottom(Stack<Integer> s , int data){
        if(s.isEmpty()){
         s.push(data);
         return;
        } 
        int top = s.pop();
        PushAtBottom(s, data);
        s.push(top);
    }
    public static void reverseStack(Stack<Integer> s){
        if(s.empty()){
            return;
        }
        int top = s.pop();
        reverseStack(s);
        PushAtBottom(s, top);
    }
    //to print a stack
    public static void printStack(Stack<Integer> s){
        while(!s.isEmpty()){
            System.out.println(s.peek());
            s.pop();
        }
    }
    
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(1);
        s.push(2);
        s.push(3);
        //below method uses O(n) space as creating a new stack
        // Stack<Integer> newStack = new Stack<>();
        // while(s.size()!=0){
        //     newStack.push(s.pop());
        // }
        // System.out.println(newStack);
        reverseStack(s);
        printStack(s);

    }

}
