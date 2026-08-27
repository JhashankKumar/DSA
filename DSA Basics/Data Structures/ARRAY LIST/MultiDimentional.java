import java.util.ArrayList;

public class MultiDimentional {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> mainlist = new ArrayList<>();// main list
        ArrayList<Integer> list1 = new ArrayList<>();// list 1
        list1.add(1);
        list1.add(2);
        mainlist.add(list1);
        ArrayList<Integer> list2 = new ArrayList<>();// list 2
        list2.add(3);
        list2.add(4);
        mainlist.add(list2);
        System.out.println(mainlist);
        // printing main list
        for (int i = 0; i < mainlist.size(); i++) {
            ArrayList<Integer> currList = mainlist.get(i);
            for (int j = 0; j < currList.size(); j++) {
                System.out.print(currList.get(j) + " ");
            }
            System.out.println();
        }

    }

}
