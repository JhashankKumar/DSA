package LinkedList;

public class CycleDetect {
    public static class Node{//class
        int data;
        Node next;
        public Node(int data){//constructor
            this.data = data;
            this.next = null;
        }
    }
    //properties
    public static Node head;
    public static Node tail;
    public static int size;
    //methods creating
    //add method
    //frist add
    public void addFrist(int data){
        //step1 - create new node
        Node newNode = new Node(data);
        size++;
        //when ever a LinkedList is created a null node will be created
        //that will be head node and due to null head and tail are assigned to null node 
        if(head == null){
            head = tail = newNode;
            return;
        }
        //step2 - newNode next = head
        //in the next of newNode the address of next node will be stored
        newNode.next = head; //this step links two nodes
        //step3 - head = newNode
        //in this step making new node as head 
        head = newNode;
    }
    //method to find wether linked list is cyclic or not
    public static boolean iscycle(){ 
        Node slow = head;
        Node fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;//+1
            fast = fast.next.next;//+2
            if(slow == fast){
                return true;//cycle exist
            }
        }
        return false;//cycle doesn't exist
    }
    public static void main(String[] args) {
        head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = head;
        System.out.println(iscycle());
    }
    
}
