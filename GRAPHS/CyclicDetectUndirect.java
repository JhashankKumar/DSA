import java.util.*;
public class CyclicDetectUndirect{
    static class Edge{
        int src;
        int dest;

        public Edge(int s, int d){
            this.src =s;
            this.dest =d ;
        }
    }
    static void createGraph(ArrayList<Edge>graph[]){
        for(int i=0;i<graph.length;i++){
            graph[i]= new ArrayList<>();
        }

        graph[0].add(new Edge(0, 1));
        graph[0].add(new Edge(0, 2));
        graph[0].add(new Edge(0, 3));

        graph[1].add(new Edge(1, 0));
        graph[1].add(new Edge(1,2));

        graph[2].add(new Edge(2,0));
        graph[2].add(new Edge(2, 1));

        graph[3].add(new Edge(3, 0));
        graph[3].add(new Edge(3, 4));

        graph[0].add(new Edge(4, 3));
    }
    public static boolean detectCycle(ArrayList<Edge>[]graph){
        boolean vis[]=new boolean[graph.length];
        for(int i=0;i<graph.length;i++){
            if(!vis[i]){
               if( detectCycleutil(graph,vis,i,-1)){
                //cycle exist in one of the part
                return true;
               }
            }
        }
        return false;
    }
    public static boolean detectCycleutil(ArrayList<Edge>[]graph,boolean vis[],int curr, int parent){
        vis[curr]= true;

        for(int i=0;i<graph[curr].size();i++){
            Edge e = graph[curr].get(i);
            //case 3
            if(!vis[e.dest]){
                if(detectCycleutil(graph,vis,e.dest,curr)){
                    return true;
                }
            }
            //case 1
            else if(vis[e.dest]&&e.dest!=parent){
                return true;
            }
            //case 2 -> do nothing -> conitnue
        }
        return false;
    }
    public static void main(String[] args) {
        int v =5;
        ArrayList<Edge> graph[]=new ArrayList[v];
        createGraph(graph);
        System.out.println(detectCycle(graph));

    }
}
