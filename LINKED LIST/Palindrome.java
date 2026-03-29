package LinkedList;

public class Palindrome {
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
    //method for finding mid
    //slow fast Approach
    public Node findMid(Node head){
        Node slow = head;
        Node fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next; //+1
            fast = fast.next.next;//+2
        }
        return slow;//slow is my mid Node
    }
    //check palindrome
    public boolean checkPalindrome(){
        if(head == null || head.next == null){
            return true;
        }
        //step 1: find mid
        Node midNode = findMid(head);
        //step 2: reverse 2nd half
        Node prev = null;
        Node curr = midNode;
        Node next;
        while(curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        Node right = prev;//right half head
        Node left = head;
        //step 3: check left half and right half 
        while(right != null){
            if(left.data != right.data){
                return false;
            }
            left = left.next;
            right = right.next;
        }
        return true;
    }
    public static void main(String[] args) {
        Palindrome ll2 = new Palindrome();
        //creating node of linkedlist
        ll2.addFrist(1);
        ll2.addFrist(2);
        ll2.addFrist(1);
        //ll2.addFrist(1);
        ll2.print();
        System.out.println(ll2.checkPalindrome());
    }
    
}
