import java.util.Stack;

public class ValidParentheses {
    public static boolean isValid(String str) {
        Stack<Integer> s = new Stack<>();
        for(int i=0; i<str.length();i++){
            char ch = str.charAt(i);
            if(ch == '('||ch== '{'||ch=='['){
                s.push((int) ch);
            }else{
                if(s.empty()){
                    return false;
                }
                if((s.peek() == '('&& ch==')')
                ||(s.peek() == '{'&& ch=='}')
                ||(s.peek() == '['&& ch==']')){
                    s.pop();
                }else{
                    return false;
                }
            }
        } 
        if(s.empty()){
            return true;
        }else{
            return false;
        } 
    }
    public static void main(String[] args) {
        String str = "[{()}]";//true
        String str2 = "(()){}[";
        System.out.println(isValid(str));
        System.out.println(isValid(str2));
    }
    
}
