import java.util.*;
public class CyclicDetectDirected {
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

        graph[0].add(new Edge(0, 2));
        
        graph[1].add(new Edge(1, 0));
        
        graph[2].add(new Edge(2, 3));

        graph[3].add(new Edge(3, 0));
        
    }    
    //this function checks wether the node already visted or not
    //if visited then check for cycle
    public static boolean iscycle(ArrayList<Edge>[]graph){
        boolean vis[]= new boolean[graph.length];
        boolean stack[]= new boolean[graph.length];

        //if a graph of different parts then cycle doesn't exist in any part
        for(int i=0; i<graph.length;i++){
            if(!vis[i]){
                if(iscycleUtil(graph,i,vis,stack)){
                    return true;
                }
            }
        }
        return false;
    }
    //here node's neighbour is checked exist in stack or not
    //if neighbour exist cycle exist else no cycle exist
    public static boolean iscycleUtil(ArrayList<Edge>[]graph,int curr,boolean vis[],boolean stack[]){
        vis[curr]=true;
        stack[curr]= true;
        for(int i=0;i<graph.length;i++){
            Edge e = graph[curr].get(i);
            if(stack[e.dest]){//cycle exist as neighbour already exist in stack
                return true;
            }
            //if neighbour visted no need to check next 
            if(!vis[e.dest]&&iscycleUtil(graph,e.dest,vis,stack)){
                return true;
            }
        }
        stack[curr]=false;
        return false;
    }

    public static void main(String[] args) {
        int v=4;
        ArrayList<Edge> graph[]= new ArrayList[v];
        createGraph(graph);
        System.out.println(iscycle(graph));
    }
    
}
