import java.util.HashSet;
import java.util.LinkedHashSet;

public class Linked_HashSet {
    public static void main(String[] args) {
        HashSet<String> cities = new HashSet<>();
        cities.add("Delhi");
        cities.add("Noida");
        cities.add("Mumbai");
        cities.add("Bengaluru");
        System.out.println(cities);

        LinkedHashSet<String> lhs = new LinkedHashSet<>();
        lhs.add("Delhi");
        lhs.add("Mumbai");
        lhs.add("Noida");
        lhs.add("Benguluru");
        System.out.println(lhs);
    }
    
}
