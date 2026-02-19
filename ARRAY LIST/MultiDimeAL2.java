import java.util.ArrayList;
public class MultiDimeAL2 {
    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>>mainlist = new ArrayList<>();
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        ArrayList<Integer> list3 = new ArrayList<>();
        //this loop for adding values into the ArrayList
        for(int i=1;i<5;i++){
           list1.add(i*1);
           list2.add(i*2);
           list3.add(i*3);
        }
        mainlist.add(list1);
        mainlist.add(list2);
        mainlist.add(list3);
        list2.remove(3);
        list2.remove(2);
        System.out.println(mainlist);
        //this loop for printing the ArrayList
        for(int i=0;i<mainlist.size();i++){
            ArrayList<Integer> currlist = mainlist.get(i);
            for(int j=0;j<currlist.size();j++){
                System.out.print(currlist.get(j)+" ");
            }
            System.out.println();
        }
    }
    
}
