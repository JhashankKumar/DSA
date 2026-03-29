import java.util.*;
public class hashMapImpliment {
    //hashmap class is created where all operations are implimented
    static class HashMap<K,V>{//K and V are generics 
        //this node class is created to store LinkedList  Node values of HASHMAP which stored in buckets of array
        private class Node{
            K key;
            V value;

            public Node(K Key , V value){
                this.key = Key;
                this.value = value;
            }
        }
        //Nodes in Array (n)
        private int n;
        private int N;
        // Array size (N)[Buckets]
        private LinkedList<Node> buckets[];

        @SuppressWarnings("unchecked")
        public HashMap(){
            this.N = 4;
            // a ARRAY is created with size 4 (4 BUCKETS)
            this.buckets = new LinkedList[4];
            //in for loop for each BUCKET a new NODE is created initially with null value
            for(int i=0;i<4;i++){
                this.buckets[i]= new LinkedList<>();

            }
        }
        //hashfunction gives bucket index
        private int hashFunction(K key){
            int hc = key.hashCode();
            return Math.abs(hc)%N;//buckets.length is N size
        }
        //search in  LL gives data index
        private int SearchInLL(K key , int bi){
            LinkedList<Node> ll = buckets[bi];
            int di = 0;
            for(int i=0;i<ll.size();i++){
                Node node = ll.get(i);
                if(node.key==key){
                    return di;
                }
                di++;
            }
            return -1;

        }
        @SuppressWarnings("unchecked")
        private void rehash(){
            LinkedList<Node> oldBuck[]= buckets;
            //new linkedList is created Buckets
            buckets = new LinkedList[N*2];
            N=2*N;
            //Ndoes are initialized at each Bucket
            for(int i=0;i<buckets.length;i++){
                buckets[i]= new LinkedList<>();
            }
            //nodes -> add in bucket
            //Nodes in old bucket is removed and kept in new bucket
            for(int i=0;i<oldBuck.length;i++){
                LinkedList<Node> ll =oldBuck[i];
                for(int j=0;j<ll.size();j++){
                    Node node = ll.remove();
                    put(node.key , node.value);
                }
            }
        }
        //all functions are implimented in O(1)
        //constant time //O(lambda) -> O(1)
        public void put(K key , V value) {
            int bi = hashFunction(key);//0 to size-1
            //di gives data index
            int di = SearchInLL(key ,bi); // key is there : valid;not there: -1
            //if condition checks wether new node need to be created or old node need to be update  
            if(di!=-1){
                Node node = buckets[bi].get(di);
                node.value = value;
            }else{
                buckets[bi].add(new Node(key, value));
                n++;
            }
            double lambda = n/N;
            if(lambda>2.0){
                rehash();
            }
        }
        public boolean containsKey(K key) {
            int bi = hashFunction(key);//0 to size-1
            //di gives data index
            int di = SearchInLL(key ,bi); // key is there : valid;not there: -1
            //if condition checks wether new node need to be created or old node need to be update  
            if(di!=-1){
               return true;
            }else{
                return false;
            }
        }
        public V remove(K key){
            int bi = hashFunction(key);//0 to size-1
            //di gives data index
            int di = SearchInLL(key ,bi); // key is there : valid;not there: -1
            //if condition checks wether new node need to be created or old node need to be update  
            if(di!=-1){
                Node node = buckets[bi].remove(di);
                n--;
                return node.value;
            }else{
                return null;
            }
        }
        public V get(K key){
            int bi = hashFunction(key);//0 to size-1
            //di gives data index
            int di = SearchInLL(key ,bi); // key is there : valid;not there: -1
            //if condition checks wether new node need to be created or old node need to be update  
            if(di!=-1){
                Node node = buckets[bi].get(di);
                return node.value;
            }else{
               return null;
            }
        }
        public ArrayList<K> keyset(){
            ArrayList<K> keys = new ArrayList<>();
            for(int i=0;i<buckets.length;i++){
                LinkedList<Node> ll = buckets[i];
                for(Node node : ll){
                    keys.add(node.key);
                }
            }
            return keys;
        }
        public boolean isEmpty(){
            return n==0;
        }
    }
    public static void main(String[] args) {
        HashMap<String,Integer> hm = new HashMap<>();
        hm.put("India", 100);
        hm.put("China", 150);
        hm.put("US", 50);

        ArrayList<String> keys = hm.keyset();
        for(String Key : keys){
            System.out.println(Key);
        }
        System.out.println(hm.get("India"));
        System.out.println(hm.remove("India"));
        System.out.println(hm.get("India"));
    }
    
}
