package LinkedList;
import java.util.LinkedList;
import java.util.Queue;
public class LLcollection {
    public static void main(String[] args) {
        LinkedList<Integer>ll = new LinkedList<>();
        ll.addLast(3);
        ll.addFirst(2);
        ll.addFirst(1);
        ll.addFirst(0);
        System.out.println(ll.indexOf(1));
        ll.removeLast();
        ll.removeFirst();
        System.out.println(ll);
    }
}
