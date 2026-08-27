import java.util.*;
public class nearByCars {
    static class point implements Comparable<point>{
        int x;
        int y;
        int disSq;
        int idx;

        public point(int x,int y,int disSq,int idx){
            this.x = x;
            this.y = y;
            this.disSq = disSq;
            this.idx =idx;

        }
        @Override
        public int compareTo(point p2) {
            return this.disSq - p2.disSq;
        }
    }
    public static void main(String[] args) {
        int pts[][]={{3,3},{5,-1},{-2,4}};
        int k =2;
        PriorityQueue<point> pq = new PriorityQueue<>();
        for(int i=0;i<pts.length;i++){
            int distsq = pts[i][0]*pts[i][0]+pts[i][1]*pts[i][1];
            pq.add(new point(pts[i][0],pts[i][1],distsq,i));
        }
        //nearest k cars
        for(int i=0;i<k;i++){
            System.out.println("c"+pq.remove().idx);
        }
    }
}
