//Kth ancestor of a node in binary tree
/*
Given a binary tree in which nodes are numbered from 1 to n. Given a node and a positive integer K. 
We have to print the Kth ancestor of the given node in the binary tree. If there does not exist any 
such ancestor then print -1.
For example in the below given binary tree, the 2nd ancestor of 5 is 1. 3rd ancestor of node 5 will be -1. 
*/
public class KthAncestor {
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
    public static int kthAncestor(Node root,int n,int k) {
        if(root == null){
            return -1;
        }
        if(root.data==n){
            return 0;
        }
        int leftDist = kthAncestor(root.left, n, k);
        int rightDist = kthAncestor(root.right, n, k);
        if(leftDist==-1&&rightDist==-1){
            return -1;
        }
        int max = Math.max(leftDist, rightDist);
        if(max+1 == k){
            System.out.println(root.data);
        }
        return max+1;
        
    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right= new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        int n = 5;int k=2;
        kthAncestor(root, n, k);

    }    
    
}
