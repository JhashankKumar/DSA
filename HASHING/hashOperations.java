import java.util.*;
public class hashOperations{
    public static void main(String[] args) {
        //create
        HashMap<String,Integer> hm = new HashMap<>();

        //insert
        hm.put("India", 100);
        hm.put("China", 150);
        hm.put("US", 50);

        //iterations
        //entry set 
        //hm.entryset();
        Set<String> keys = hm.keySet();
        System.err.println(keys);
        for(String k : keys){
            System.out.println("key: "+k+" ,values: "+hm.get(k));
        }

        System.out.println(hm);

        //size
        System.out.println(hm.size());

        //get
        int population = hm.get("India");
        System.out.println(population);

        System.out.println(hm.get("indonesia"));

        //contains Key 
        System.out.println(hm.containsKey("India"));//true
        System.out.println(hm.containsKey("indonesia"));

        //remove
        System.out.println(hm.remove("China"));

        System.out.println(hm);

        //Is Empty
        System.out.println(hm.isEmpty());
        hm.clear();
        System.out.println(hm.isEmpty());
    }
}