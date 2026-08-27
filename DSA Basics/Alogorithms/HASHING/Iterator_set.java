import java.util.HashSet;
import java.util.Iterator;

public class Iterator_set {
    public static void main(String[] args) {
        HashSet<String> cities = new HashSet<>();
        cities.add("Delhi");
        cities.add("Mumbai");
        cities.add("Noida");
        cities.add("Benguluru");

        //interface Iterator 
        Iterator it = cities.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }

        //advanced iterators
        for(String city: cities){
            System.out.println(city);
        }
            
    }
    
}
