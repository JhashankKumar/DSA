package Array_List;
import java.util.ArrayList;
import java.util.Collections;

public class sorting {
    public static void main(String[] args) {
        ArrayList<Integer>list = new ArrayList<>();
        list.add(2);
        list.add(5);
        list.add(9);
        list.add(3);
        list.add(6);
        list.add(8);
        System.out.println(list);
        Collections.sort(list);//asending order sort
        System.out.println(list);
        //for decending order
        Collections.sort(list,Collections.reverseOrder());
        System.out.println(list);
    }
    
}
