import java.util.Comparator;
import java.util.PriorityQueue;;;
public class basicPQ {
    public static void main(String[] args) {
        //comparator.reverseOrder reverse the order 
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        pq.add(3);
        pq.add(4);
        pq.add(1);
        pq.add(7);

        while(!pq.isEmpty()){
            System.out.println(pq.peek());//O(1)
            pq.remove();//O(log n)
        }
    }
    
}
