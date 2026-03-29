public class MirrorBST {
    static class Node{
        int data;
        Node left;
        Node right;
        Node(int data){
            this.data = data;
            this.left= null;
            this.right= null;
        }
    } 
    private static Node mirrorbst(Node root) {
        if(root == null){
            return null;
        }
        Node leftmirror=mirrorbst(root.left);
        Node rightmirror = mirrorbst(root.right);

        root.left = rightmirror;
        root.right = leftmirror;
        return root;
        
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
        Node root = new Node(8);
        root.left = new Node(5);
        root.right= new Node(10);
        root.left.left = new Node(3);
        root.left.right = new Node(6);
        root.right.right = new Node(11);
        preorder(root);
        System.out.println();
        root = mirrorbst(root);
        preorder(root);
    }
}
