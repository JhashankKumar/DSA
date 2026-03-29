import java.util.*;
public class TopologicalSort {
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

        graph[2].add(new Edge(2,3));
        
        graph[3].add(new Edge(3,1));
        
        graph[4].add(new Edge(4,0));
        graph[4].add(new Edge(4,1));

        graph[5].add(new Edge(5, 0));
        graph[5].add(new Edge(5,2));
        
    }  
    //Topological Sort Using DFS
    public static void topsortDFS(ArrayList<Edge>[]graph) {
        boolean vis[]= new boolean[graph.length];
        Stack<Integer> s = new Stack<>();

        for(int i=0;i<graph.length;i++){
            if(!vis[i]){
                topsortDFSUtil(graph,i,vis,s); // modified DFS
            }
        }
        while(!s.isEmpty()){
            System.out.print(s.pop()+" ");
        }
        System.out.println();
    } 
    public static void topsortDFSUtil(ArrayList<Edge>[] graph, int curr , boolean vis[], Stack<Integer> s){
        vis[curr]= true;

        for(int i=0;i<graph[curr].size();i++){
            Edge e = graph[curr].get(i);
            if(!vis[e.dest]){
                topsortDFSUtil(graph,e.dest, vis, s);
            }
        }
        s.push(curr);
    }
    //Topological Sort Using BFS

    //calcIndeg function will calculate each vertex in-degree 
    public static void calcIndeg(ArrayList<Edge>graph[],int indeg[]){
        for(int i=0;i<graph.length;i++){
            int v = i;
            for(int j=0;j<graph[v].size();j++){
                Edge e = graph[v].get(j);
                indeg[e.dest]++;
            }
        }
    }
    public static void topsortBFS(ArrayList<Edge>[]graph){
        int indeg[]= new int[graph.length];
        calcIndeg(graph, indeg);
        Queue<Integer> q = new LinkedList<>();

        //here the vertex whose in-degree is zero it was called into queue
        for(int i=0;i<indeg.length;i++){
            if(indeg[i]==0){
                q.add(i);
            }
        }

        //BFS
        while(!q.isEmpty()){
            int curr = q.remove();
            System.err.print(curr+" "); //topological sort printing

            //here checking for neighbours of vertex 
            //and decreasing its indeg value
            for(int i=0;i<graph[curr].size();i++){
                Edge e = graph[curr].get(i);
                indeg[e.dest]--;
                if(indeg[e.dest]==0){
                    q.add(e.dest);
                }
            }
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int v =6;
        ArrayList<Edge> graph[]=new ArrayList[v];
        createGraph(graph);
        topsortDFS(graph);
        topsortBFS(graph);
    } 
}
