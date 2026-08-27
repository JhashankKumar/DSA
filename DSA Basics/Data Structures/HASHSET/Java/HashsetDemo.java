import java.util.*;;
public class HashsetDemo {
    public static void main(String[] args) {
        Set<String> hashset =  new HashSet();
        hashset.add("A");
        hashset.add("B");
        //here we are checking duplicate are not allowed in hashset
        boolean r1 = hashset.add("C");
        System.out.println(r1);
        boolean r2 = hashset.add("C");
        System.out.println(r2);
        System.out.println(hashset);
        hashset.remove("A");
        System.out.println(hashset);
        System.out.println(hashset.contains("A"));      
    }   
}