public class AVLTree {
    static class Node{
        int data , height;
        Node left ,right;
        Node(int data){
            this.data = data;
            height =1;
        }
    }
    public static Node root;
    //height function returns each node root to it
    public static int  Height(Node root) {
        if(root == null){
            return 0;
        }
        return root.height;
    }
    //Get Balane function
    public static int getBalance(Node root){
        if(root == null){
            return 0 ;
        }
        return Height(root.left)-Height(root.right);
    }
    //left rotate subtree rooted with x
    public static Node leftRotate(Node x){
        Node y = x.right;
        Node T2 = y.left;
        //perform rotation
        y.left = x;
        x.right = T2;
        //update heights
        x.height = Math.max(Height(x.left),Height(x.right))+1;
        y.height = Math.max(Height(y.left),Height(y.right))+1;
        //Return new root
        return y;
    }
    //right rotate subtree rooted with y
    public static Node rightRotate(Node y){
        Node x = y.left;
        Node T2 = x.right;
        //perform rotation
        x.right = y;
        y.left = T2;

        //update heights
        y.height = Math.max(Height(y.left),Height(y.right))+1;
        x.height = Math.max(Height(x.left),Height(x.right))+1;
        //Return new root
        return x;
    }
    //insert function
    //it will insert node according to BST properties
    public static Node insert(Node root,int key){
        if(root == null){
            return new Node(key);
        }
        if(key<root.data){
            root.left = insert(root.left, key);
        }else if(key > root.data){
            root.right = insert(root.right, key);
        }else{
            return root; // duplicates are not allowed
        }
        //update root height
        root.height = 1+Math.max(Height(root.left),Height(root.right));
        //get root's balance factor 
        int bf = getBalance(root);
        //Left Left Case 
        if(bf>1&&key<root.left.data){
            return rightRotate(root);
        }
        //Right Right Case
        if(bf<-1&&key>root.right.data){
            return leftRotate(root);
        }
        //Left Right  case 
        if(bf>1&&key>root.left.data){
            root.left = leftRotate(root.right);
            return rightRotate(root);
        }
        //Right Left Case
        if(bf<-1&&key<root.right.data){
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root; // returned if AVL balanced

    }
    public static void preorder(Node root) {
        if(root == null){
            return;
        }
        System.out.print(root.data+" ");
        preorder(root.left);
        preorder(root.right);
        
    }
    public static void main(String[] args) {
        root = insert(root,10);
        root = insert(root,20);
        root = insert(root,30);
        root = insert(root,40);
        root = insert(root,50);
        root = insert(root,25);
        preorder(root);        
    }
    
}
