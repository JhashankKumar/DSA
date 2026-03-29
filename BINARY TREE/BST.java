import java.util.ArrayList;

public class BST {
    static class Node{
        int data;
        Node right;
        Node left;

        Node(int data){
            this.data = data;
        }
    }
    public static void inorder(Node root) {
        if(root == null){
            return;
        }
        inorder(root.left);
        System.out.print(root.data+" ");
        inorder(root.right);
        
    }
    //insert function will insert a Node in BST and returns a Node type value
    //that Node is root
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
    public static Node  delete(Node root , int val) {
        if(root.data<val){
            root.right = delete(root.right , val);
        }
        if(root.data>val){
            root.left =  delete(root.left, val);
        }
        else{//case -1: Leaf Node
            if(root.left==null&&root.right==null){
                return null;
            }
            //case-2: single child
            if(root.left== null){
                return root.right;
            }
            if(root.right==null){
                return root.left;
            }
            //case-3: both children
            Node IS = findInorderSuccessor(root.right);
            root.data = IS.data;
            root.right = delete(root.right, IS.data);
        }
        return root;
    }
    public static Node findInorderSuccessor(Node root){
        while(root.left!=null){
            root = root.left;
        }
        return root;
    }
    public static void printInRange(Node root , int k1,int k2){
        if(root == null){
            return;
        }
        if(root.data>=k1&&root.data<=k2){
            printInRange(root.left, k1, k2);
            System.out.print(root.data+" ");
            printInRange(root.right, k1, k2);
        }else if(root.data<k1){
            printInRange(root.left, k1, k2);
        }else{
            printInRange(root.right, k1, k2);
        }
    }
    public static void printPath(ArrayList<Integer>path) {
        for(int i=0;i<path.size();i++){
            System.out.print(path.get(i)+"->");
        }
        System.out.println("null");
        
    }
    public static void RootToLeaf(Node root,ArrayList<Integer>path) {
        if(root == null){
            return;
        }
        path.add(root.data);
        if(root.right==null&&root.left==null){
            printPath(path);
        }
        RootToLeaf(root.left, path);
        RootToLeaf(root.right, path);
        path.remove(path.size()-1);
    }
    public static boolean isValidBST(Node root , Node min,Node max) {
        if(root == null){
            return true;
        }
        if(min!=null&&root.data<=min.data){
            return false;
        }
        if(max!=null&&root.data>=max.data){
            return false;
        }
        return isValidBST(root.right,root, max)&&isValidBST(root.left, min, root);
    }
    public static void main(String[] args) {
        //int values[]={1,3,2,4,6,5,7,8,10,9};
        int values2[]= {8,5,3,1,4,6,10,11,14};
        //for isValidBST
        //int values2[] = {1,1,1};
        Node root = null;
        for(int i=0;i<values2.length;i++){
            root = insert(root, values2[i]);
        }
        // inorder(root);
        // System.out.println();
        // root = delete(root, 1);
        // inorder(root);
        // System.out.println();
        // printInRange(root, 5, 12);
        // System.out.println();
        // RootToLeaf(root,new ArrayList<>());
        if(isValidBST(root, null , null)){
            System.out.println("valid");
        }
        else{
            System.out.println("invalid");
        }
    }
    
}
