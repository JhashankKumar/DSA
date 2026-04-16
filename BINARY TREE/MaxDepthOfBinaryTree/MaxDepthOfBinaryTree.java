package MaxDepthOfBinaryTree;
/*
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
*/
public class MaxDepthOfBinaryTree {
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

    public static int maxDepth(Node root){
        if(root == null){
            return 0;
        }
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth)+1;
    }

    public static void main(String[] args) {
        // array of nodes to create the binary tree with null values for leaf nodes
        // int nodes[] = {1,2,3,4,5,6,7};
        // Integer nodes[] = {1, null , 2, null, null, null, 3};
        Integer nodes[] = {1, 2, 3, null, 4, null, null};
        Node root = createTree(nodes, 0);
        System.out.println(maxDepth(root));
    }

    public static Node createTree(Integer nodes[], int index){
        if(index>=nodes.length || nodes[index] == null){
            return null;
        }
        Node newNode = new Node(nodes[index]);
        newNode.left = createTree(nodes, 2*index+1);
        newNode.right = createTree(nodes, 2*index+2);
        return newNode;
    }
}
