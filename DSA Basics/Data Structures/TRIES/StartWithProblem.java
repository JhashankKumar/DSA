public class StartWithProblem {
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
    public static boolean StartWith(String prefix){
        Node curr = root;
        for(int i=0;i<prefix.length();i++){
            int idx = prefix.charAt(i)-'a';
            if(curr.childern[idx]==null){
                return false;
            }
            curr = curr.childern[idx];
        }
        return true;
    }
    public static void main(String[] args) {
        String words[]={"apple","app","mango","man","women"};
        String prefix1 = "app";
        String prefix2 = "moon";
        for(int i=0;i<words.length;i++){
            insert(words[i]);
        }
       System.out.println(StartWith(prefix1));
       System.out.println(StartWith(prefix2));
    }
    
}
