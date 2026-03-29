public class LongestWordPrefix {
    static class Node{
        Node childern[]= new Node[26];
        boolean eow;
        public Node(){
            for(int i=0;i<26;i++){
                childern[i]=null;
            }
        }
    }
    public static Node root = new Node();

    public static void insert(String word){
        int level = 0 ;
        int len = word.length();
        int idx= 0;
        Node curr = root;
        for(;level<len;level++){
            idx= word.charAt(level)-'a';
            if(curr.childern[idx]==null){
                curr.childern[idx]= new Node();
            }
            curr = curr.childern[idx];
        }
        curr.eow = true;
    }
    public static boolean search(String key){
        int level =0;
        int len = key.length();
        int idx = 0;
        Node curr = root;
        for(;level<len;level++){
            idx = key.charAt(level)-'a';
            if(curr.childern[idx]==null){
                return false;
            }
            curr = curr.childern[idx];
        }
        return curr.eow == true;
    }
    public static String ans = " ";
    public static void longestWord(Node root,StringBuilder temp){
        if(root == null){
            return ;
        }
        for(int i=0;i<26;i++){//a,b,c,d lexigographically word find
            //we need apply insted of apple 
            //for that for loop must be like
            //for(int i=25;i>=0;i++)
            if(root.childern[i]!=null&&root.childern[i].eow == true){
                char ch = (char)(i+'a');
                temp.append(ch);
                if(temp.length()>ans.length()){
                    ans = temp.toString();
                }
                longestWord(root.childern[i], temp);
                temp.deleteCharAt(temp.length()-1);//backtarck
            }
        }
    }
    public static void main(String[] args) {
        String[] words = {"a","banana","app","ap","apply","appl","apple"};
        //inserting into TRIES
        for(int i=0;i<words.length;i++){
           insert(words[i]);
        }
        longestWord(root, new StringBuilder(" "));
        System.out.println(ans);
    }
}
