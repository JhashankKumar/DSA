import java.util.*;
public class DequeCF {
    public static void main(String[] args) {
        Deque<Integer> deque = new LinkedList<>();
        deque.addFirst(1);//1
        deque.addFirst(2);//2 1
        deque.addLast(3);//3 2 1
        deque.addLast(4);//4 3 2 1
        deque.addLast(5);//5 4 3 2 1
        System.out.println(deque);
        System.out.println(deque.removeLast());
        System.out.println(deque);

    }
    
}
