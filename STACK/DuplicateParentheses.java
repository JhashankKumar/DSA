

import java.util.Stack;

public class DuplicateParentheses {
    public static boolean duplicateparentheses(String str) {
        Stack<Integer> s = new Stack<>();
        for(int i = 0;i<str.length();i++){
            char ch = str.charAt(i);
            //closing
            if(ch ==')'){
                int count = 0;
                while(s.peek() != '('){
                    s.pop();
                    count++;
                }
                if(count < 1){
                    return true; // duplicate
                }else{
                    s.pop(); //opening pair
                }
            }else{
                //opening
                s.push((int) ch);
            }
        }
        return false;
    }
    public static void main(String[] args) {
        //valid string is to be given 
        String str = "((a+b))";//false
        String str1 = "(a+b)";//true
        System.out.println(duplicateparentheses(str));
        System.out.println(duplicateparentheses(str1));
    }
    
}
