import java.util.*;
public class string1 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String name;
            String sername;
            name = sc.nextLine();
            sername = sc.nextLine();
            System.out.println(name+" "+sername);
            System.out.println(name);//print string
            System.out.println(name.length());//print lenght of string
            System.out.println(name.charAt(3));//print character at index
        }
    }    
}