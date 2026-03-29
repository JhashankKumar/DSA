import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class ActivitySelect{
    public static void main(String[] args) {
        int start[]= {1, 3, 0, 5, 8, 5};
        int end[]= {2, 4, 6, 7, 9, 9};
        //end time basis sorted
        int maxAct = 0;
        ArrayList<Integer> ans = new ArrayList<>();

        //max activity
        maxAct=1;
        ans.add(0);
        int lastend = end[0];
        for(int i=1;i<end.length;i++){
            if(start[i]>=lastend){
                maxAct++;
                ans.add(i);
                lastend = end[i];
            }
        }
        System.out.println("max activity"+ " "+maxAct);
        for(int i=0;i<ans.size();i++){
            System.out.print("A"+ans.get(i)+" ");
        }
        System.out.println();
        sort();
    }
    // this function is used when end time  is not sorted
    public static void sort(){
        int start[]= {0, 1, 3, 5, 5, 8};
        int end[]={6, 2, 4, 7, 9, 9};
        //sorting 
        int activities[][]=new int[start.length][3];
        for(int i=0;i<start.length;i++){
            activities[i][0]=i;
            activities[i][1]=start[i];
            activities[i][2]= end[i];
        }
        //lamda function 
        Arrays.sort(activities,Comparator.comparingDouble(o->o[2]));


        //end time basis sorted
        int maxAct = 0;
        ArrayList<Integer> ans = new ArrayList<>();

        //max activity
        maxAct=1;
        ans.add(activities[0][0]);
        int lastend = activities[0][2];
        for(int i=1;i<end.length;i++){
            if(activities[i][1]>=lastend){
                //activity select
                maxAct++;
                ans.add(activities[i][0]);
                lastend = activities[i][2];
            }
        }
        System.out.println("max activity"+ " "+maxAct);
        for(int i=0;i<ans.size();i++){
            System.out.print("A"+ans.get(i)+" ");
        }
        System.out.println();

    }
}    

