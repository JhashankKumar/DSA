package Array_List;
import java.util.ArrayList;

public class MaxNum {
    public static void main(String[] args) {
    ArrayList<Integer>list = new ArrayList<>();
    list.add(2);
    list.add(5);
    list.add(9);
    list.add(3);
    list.add(6);
    list.add(8);
    int max1= Integer.MIN_VALUE;
    int max2 = Integer.MIN_VALUE;
    for(int i=0;i<list.size();i++){
        //method 1
        if(max1<list.get(i)){
            max1 = list.get(i);
        }
    }
    //method 2
    for(int j=0;j<list.size();j++){
        max2 = Math.max(max2, list.get(j));
    }  
    System.out.println("max element"+" " +max1);
    System.err.println("max element"+" "+max2);
    }
}    
    
