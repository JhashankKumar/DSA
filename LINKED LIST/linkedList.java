public class linkedList {
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
    //last add
    public void addLast(int data){
        //creating a node
        Node newNode = new Node(data);
        size++;
        if(head == tail){
            head = tail = newNode;
            return;
        }
        //in this tail.next step the newNode address is stored in the tail node 
        tail.next = newNode;
        //now making newNode as tail
        tail = newNode;
    }
    //middle add
    public void addMiddle(int idx,int data){
        if(idx==0){
            addFrist(data);
            return;
        }
        Node newnode = new Node(data);
        size++;
        Node temp = head;
        int i=0;
        while(i<idx-1){
            temp=temp.next;
            i++;
        }
        //i = idx-1; temp -> prev
        newnode.next = temp.next;
        temp.next = newnode;
    }//remove method
    //frist remove
    public int removeFrist(){
        if(size ==0){
            System.out.println("LL is empty");
            return Integer.MIN_VALUE;
        }else if(size==1){
            int val= head.data;
            head = tail= null;
            size=0;
            return val;
        }                  
        int val = head.data;
        head = head.next;
        size--;
        return val;
    }
    //last remove 
    public int removeLast(){
        if(size ==0){
            System.out.println("LL is empty");
            return Integer.MIN_VALUE;
        }else if(size==1){
            int val = head.data;
            head = tail= null;
            size=0;
            return val;
        }
        //previous: i= size-2
        Node prev = head;
        for(int i=0;i<size-2;i++){
            prev=prev.next;
        }
        int val = prev.next.data;//tail.data
        prev.next = null;
        tail = prev;
        size--;
        return val;
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
    //iterator search
    public int itrsearch(int key){
        Node temp = head;
        int i=0;
        while(temp != null){
            if(temp.data == key){//key found
                return i;
            }
            temp=temp.next;
            i++;
        }
        //key not found 
        return -1;
    }
    //searching using recursive search
    public int helper(Node head,int key){
        if(head == null){
            return -1;
        }
        if(head.data == key){
            return 0;
        }
        int idx = helper(head.next, key);
        if(idx == -1){
            return -1;
        }
        return idx+1;
    }
    //reverse a linked list method
    public void reverse(){
        Node prev = null;
        Node curr = tail = head;
        Node next;
        while(curr!=null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;

    }
    public int reSearch(int key){
        return helper(head,key);
    }
    //method to delete a node in linked list
    public void deleteNthfromEnd(int n){
        //size calculation
        int sz = 0;
        Node temp= head;
        while(temp != null){
            temp = temp.next;
            sz++;
        }
        //if head need to be deleted
        if(n == sz){
            head = head.next;//remove frist
            return;
        }
        //sz-n
        //Nth node from end is equal to (size - n +1)
        //by finding the Node we can remove next node by just changing the previous node next value 
        int i = 1;
        int iToFind = sz - n;
        Node prev = head;
        while(i< iToFind){
            prev = prev.next;
            i++;
        }
        prev.next = prev.next.next;
        return;

    }
    public static void main(String[] args) {
        linkedList ll = new linkedList();
        //creating node of linkedlist
        ll.print();
        ll.addFrist(2);
        ll.print();
        ll.addFrist(1);
        ll.print();
        ll.addLast(3);
        ll.print();
        ll.addLast(4);
        ll.print();
        ll.addMiddle(0, 9);
        ll.print();
        System.out.println(size);
        ll.removeFrist();
        ll.print();
        System.out.println(size);
        ll.removeLast();
        ll.print();
        System.out.println(size);
        System.out.println(ll.itrsearch(3));
        System.err.println(ll.itrsearch(10));
        System.out.println(ll.reSearch(3));
        System.out.println(ll.reSearch(10));
        ll.print();
        ll.reverse();
        ll.print();
        ll.deleteNthfromEnd(2);
        ll.print();
        System.out.println();
    }
}