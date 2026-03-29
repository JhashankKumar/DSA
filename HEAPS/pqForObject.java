import java.util.PriorityQueue;
public class pqForObject {
    public class student implements Comparable<student>{ //overriding
        String name ;
        int rank ;

        public student(String name , int rank){
            this.name = name;
            this.rank = rank;
        }
        
        @Override
        public int compareTo(student s2){
            return this.rank - s2.rank;
        }
    }
    public static void main(String[] args) {
        PriorityQueue<student> pq = new PriorityQueue<>();
        pq.add(new student("A", 2));
        pq.add(new student("B", 6));
        pq.add(new student("C", 10));
        while(!pq.isEmpty()){
            System.out.println(pq.peek().name+ "-> "+pq.peek().rank);//O(1)
            pq.remove();//O(logn)
        }

        
    }
    
}
