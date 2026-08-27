package LinkedList;
public class MergeSort {
    public static class Node{//class
        int data;
        Node next;
        public Node(int data){//constructor
            this.data = data;
            this.next = null;
        }
    }
    //properties
    public Node head;
    public static Node tail;
    public void addFirst(int data){
        //step1 - create new node
        Node newNode = new Node(data);
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
    //for finding mid 
    private static Node getMid(Node head){
        Node slow = head;
        Node fast = head.next;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;//mid
    }
    private static Node merge(Node head1,Node head2){
        Node mergedLL = new Node(-1);
        Node temp = mergedLL;
        //comparing left merge sorted ll and right merge sorted ll
        while(head1 != null && head2 != null){
            if(head1.data <= head2.data){
                temp.next = head1;
                head1 = head1.next;
                temp = temp.next;
            }
            else{
                temp.next = head2;
                head2 = head2.next;
                temp = temp.next;
            }
        }
        //after comparison remaining elements
        while(head1 != null){
            temp.next = head1;
            head1 = head1.next;
            temp = temp.next;
        }
        while(head2 != null){
            temp.next = head2;
            head2 = head2.next;
            temp = temp.next;
        }
        return mergedLL.next;
    }
    public static Node Mergesort(Node head){
        if(head == null || head.next == null){
            return head;
        }
        //find mid 
        Node mid = getMid(head);
        //left and right Merge sort
        Node righthead = mid.next;
        mid.next = null;
        Node newleft = Mergesort(head);
        Node newright = Mergesort(righthead);
        //merge 
        return merge(newleft, newright);
    }
    
    public static void main(String[] args) {
        MergeSort ll = new MergeSort();
        ll.addFirst(1);
        ll.addFirst(2);
        ll.addFirst(3);
        ll.addFirst(4);
        ll.addFirst(5);
        ll.print();
        ll.head =  Mergesort(ll.head);
        ll.print();
    }
}
