public class SearchInBST {
    static class Node{
        int data;
        Node left;
        Node right;

        public  Node(int data){
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
    public static Node  insert(Node root , int val) {
        if(root == null){
            root = new Node(val);
            return root;
        }
        if(root.data>val){
            //left sub tree
            root.left = insert(root.left, val);
        }else{
            // right subtree
            root.right = insert(root.right, val);
        }
        return root;
        
    }
    public static boolean search(Node root,int key) {
        if(root == null){
            return false;
        }
        if(root.data == key){
            return true;
        }
        if(root.data>key){
            return search(root.right, key);
        }else{
            return search(root.left, key);
        }
    }
    public static void main(String[] args) {
        int values[]={1,3,2,4,6,5,7,8,10,9};
        Node root = null;
        for(int i=0;i<values.length;i++){
            root = insert(root, values[i]);
        }
        if(search(root, 11)){
            System.out.println("found");
        }else{
            System.out.println("no found");
        }
        
    }
    
}
