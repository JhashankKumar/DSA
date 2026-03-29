import java.util.LinkedHashMap;

public class Linked_Hash_Map {
    public static void main(String[] args) {
        LinkedHashMap<String,Integer> lhm = new LinkedHashMap<>();
        lhm.put("India", 50);
        lhm.put("US", 100);
        lhm.put("China", 150);
        System.out.println(lhm);
    }
}
