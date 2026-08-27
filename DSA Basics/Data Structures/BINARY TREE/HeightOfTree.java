
public class HeightOfTree {
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

    public static int height(Node root){
        //base case 
        if(root==null){
            return 0 ;
        }
        int lh = height(root.left);
        int rh = height(root.right);
        return Math.max(lh, rh)+1;
    }
    public static int count(Node root){
        if(root == null){
            return 0;
        }
        int leftcount = count(root.left);
        int rightcount = count(root.right);
        return leftcount+rightcount+1;
    }
    public static int sum(Node root){
        if(root == null){
            return 0;
        }
        int leftsum = sum(root.left);
        int rightsum = sum(root.right);
        return leftsum+rightsum+root.data;
    }
    public static int diameter(Node root){
        if(root == null){
            return 0;
        }
        int leftdiam = diameter(root.left);
        int rightdiam = diameter(root.right);
        int leftHt = height(root.left);
        int rightHt = height(root.right);
        int selfDiam = leftHt+rightHt+1;
        return Math.max(selfDiam,Math.max(leftdiam,rightdiam));
    }
    static class Info{
        int diam;
        int ht;
        public Info(int diam,int ht){
            this.diam = diam;
            this.ht = ht;
        }
    }
    public static Info diameter2(Node root){
        if(root == null){
            return new Info(0, 0);
        }
        Info leftInfo = diameter2(root.left);
        Info rightInfo = diameter2(root.right);
        int diam = Math.max(Math.max(leftInfo.diam,rightInfo.diam),leftInfo.ht+rightInfo.ht+1);
        int ht = Math.max(leftInfo.ht,rightInfo.ht);
        return new Info(diam, ht);
    }

    public static void main(String[] args) {
        // Node root = new Node(1);
        // root.left = new Node(2);
        // root.right= new Node(3);
        // root.left.left = new Node(4);
        // root.left.right = new Node(5);
        // root.right.left = new Node(6);
        // root.right.right = new Node(7);
        // System.out.println(height(root));
        // System.out.println(count(root));
        // System.out.println(sum(root));
        // System.out.println(diameter(root));
        // System.out.println(diameter2(root).ht);
        
        //array representation of tree
        int nodes[] = {1,2,3,4,5,6,7};
        Node root = createTree(nodes, 0);
        System.out.println(height(root));
            
    }

    public static Node createTree(int nodes[], int index){
        if(index>=nodes.length){
            return null;
        }
        Node newNode = new Node(nodes[index]);
        newNode.left = createTree(nodes, 2*index+1);
        newNode.right = createTree(nodes, 2*index+2);
        return newNode;
    }
}
