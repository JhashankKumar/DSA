package LinkedList;

public class ZigZag {
     //creating an linked list using class and object 
     public static class Node{ //class
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
    public void addFirst(int data){
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
    //print method
    public void print(){
        if(head == null){
            System.err.println("ll is empty");
            return;
        }
        Node temp = head;
        while(temp != null){
            System.out.print(temp.data+"->");
            temp = temp.next;
        }
        System.out.println("null");
    }
    public void zigzag(){
        //step 1
        //find mid
        Node slow = head;
        Node fast = head.next;
        while(fast!= null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        Node mid = slow;
        //step 2
        //reverse 2nd half
        Node curr = mid.next;
        mid.next = null;
        Node prev = null;
        Node next;
        while(curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        Node left = head;
        Node right =  prev;
        Node nextL;
        Node nextR;
        //step 3
        //alter merge or zig-zag merge
        while(left != null && right != null){
            nextL = left.next;
            left.next = right;
            nextR = right.next;
            right.next = nextL;

            left = nextL;
            right = nextR;

        }
    }
    public static void main(String[] args) {
        ZigZag ll = new ZigZag();
        ll.addFirst(1);
        ll.addFirst(2);
        ll.addFirst(3);
        ll.addFirst(4);
        ll.addFirst(5);
        ll.print();
        //5->4->3->2->1->null
        //5->1->4->2->3->null
        ll.zigzag();
        ll.print();

    }
    
}
