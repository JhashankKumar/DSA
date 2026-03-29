import java.util.*;
public class FractionalKnapsack {
    public static void main(String[] args) {
        int val[]={60, 100, 120};
        int weight[]={10, 20, 30};
        int w=50;
        //this 2-D array is for ratio storing
        double ratio[][]= new double[val.length][2];
        //0th col => idx ;1st col => ratio
        for(int i=0;i<ratio.length;i++){
            ratio[i][0]=i;
            ratio[i][1]= val[i]/(double)weight[i];
        }
        //ascending order lambda function
        //sorted on bases of ratios values in ascending
        Arrays.sort(ratio,Comparator.comparingDouble(o->o[1]));

        //but we need decending order values so for loop is runned from last idx to frist idx
        int capacity = w;
        int finalValue= 0;
        for(int i=ratio.length-1;i>=0;i--){
            int idx = (int)ratio[i][0];
            if(capacity>=weight[idx]){//include full item
                finalValue += val[idx];
                capacity -= weight[idx];
            }else{
                //include fractional item
                finalValue += (ratio[i][1]*capacity);
                capacity=0;
                break;
            }
        }
        System.out.println(finalValue);
    }  
}
