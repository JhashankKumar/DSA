import java.util.Map.Entry;
import java.util.HashMap;
import java.util.Map;
public class HashMapDemo {
    public static void main(String[] args) {
        Map<String,Integer> map = new HashMap<>();
        map.put(":a",1);
        map.put("b",2);
        map.put("c",3);
        // System.out.println("Size of Map is"+" "+map.size());
        // System.out.println(map);
        if(map.containsKey("a")){
            Integer a = map.get("a");
            System.out.println("value of a"+" "+a);
        }
        //prints all keys and values in a map
        for(String key : map.keySet()){
            System.out.println("key:"+ key+",value:"+map.get(key));
        }
        //it also similary prints keys and values
        for(Entry<String, Integer> entry : map.entrySet()){
            System.out.println("KEY:"+entry.getKey()+",Value:"+entry.getValue());

        }


    }
    
}
