
import java.util.Stack;

public class ReverseString{
    public static String reverseString(String str){
        Stack<Character> s = new Stack<>();
        int idx = 0;
        //this condition will push each character as stack from string
        while(idx < str.length()){
            s.push(str.charAt(idx));
            idx++;
        }
        //this string builder is used for creating new reversed string
        StringBuilder result = new StringBuilder("");
        while(!s.isEmpty()){
            char curr = s.pop();
            result.append(curr);
        }
        return result.toString();
    }
    public static void main(String[] args) {
        String str = "abc";
        String result = reverseString(str);
        System.out.println(result);
    }

}
    
