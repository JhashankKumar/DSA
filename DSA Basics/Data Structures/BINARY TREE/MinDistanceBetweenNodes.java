public class MinDistanceBetweenNodes {
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
    public static Node lca2(Node root,int n1,int n2){
        if(root==null){
            return null;
        }
        if(root.data==n1||root.data==n2){
            return root;
        }
        Node lcaLeft = lca2(root.left, n1, n2);
        Node lcaRight = lca2(root.right, n1, n2);

        //leftLCA = val rightLCA = null
        if(lcaRight==null){
            return lcaLeft;
        }
        if(lcaLeft==null){
            return lcaRight;
        }
        return root;

    }
    public static int  lcaDis(Node root, int n) {
        if(root ==null){
            return -1;
        }
        if(root.data==n){
            return 0 ;
        }
        int leftdis = lcaDis(root.left, n);
        int rightdis = lcaDis(root.right, n);

        if(leftdis==-1&&rightdis==-1){
            return -1;
        }else if(leftdis==-1){
            return rightdis+1;
        }else{
            return leftdis+1;
        }

        
    }
    public static int minDis(Node root,int n1,int n2) {
        Node lca = lca2(root, n1, n2);
        int dis1 = lcaDis(lca,n1);
        int dis2 = lcaDis(root, n2);
        return dis1+dis2;

        
    }
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right= new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);


        int n1 =4 , n2 = 7;
        System.out.println(minDis(root, n1, n2));
        
    }
    
}
