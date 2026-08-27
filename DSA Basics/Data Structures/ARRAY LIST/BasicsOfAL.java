import java.util.ArrayList;

public class BasicsOfAL {
    public static void main(String[] args) {
        // declaring ArrayList
        // ClassName ObjectName = new ClassName()
        ArrayList<Integer> list = new ArrayList<>();
        // ArrayList<Integer>list1 = new ArrayList<>();
        // ArrayList<Integer>list2 = new ArrayList<>();
        // ArrayList<Integer>list3 = new ArrayList<>();
        // add operator in ArrayList
        // here value is placed
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        System.out.println(list.contains(1));
        System.out.println(list);
        // printing elements in an Array list
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " ");
        }
        System.out.println();
        // printing elements Order in reverse in an ArrayList
        for (int j = list.size() - 1; j >= 0; j--) {
            System.out.print(list.get(j) + " ");
        }
        System.out.println();
        // ArrayList has another add property
        // adding an element at particular index
        list.add(1, 10);
        System.out.println(list);
        // get operator in ArrayList
        // here index is placed
        int element = list.get(2);
        System.out.println(element);
        // remove operator in ArrayList
        // here also index is placed
        list.remove(2);
        System.out.println(list);
        // set operator in ArrayList
        list.set(2, 8);
        System.out.println(list);
        // contains element
        Boolean contain = list.contains(2);
        System.out.println(contain);

    }
}
