import java.util.Collections;

import java.util.*;
public class Chocola {
    public static void main(String[] args) {
        //n is number of rows
        //m is number of columns
        int n=4;int m=6;
        Integer costver[]={2,1,3,1,4};//m-1
        Integer costhor[]={4,1,2};//n-1
        Arrays.sort(costver,Collections.reverseOrder());
        Arrays.sort(costhor,Collections.reverseOrder());

        int h = 0; int v = 0; // these h and v are used for index values of cost of horizonal and vertical cuts
        int hp = 1; int vp = 1;// these hp and vp are used for how many pices are done in horizontal and vertical
        int cost = 0;

        //to cover all horizontal cuts and vertical cuts
        while(h<costhor.length&&v<costver.length){//horizontal cuts condition
            if(costver[v]<=costhor[h]){
                cost += (costhor[h]*vp);
                hp++;
                h++;
            }else{//vertical cuts
                cost += (costver[v]*hp);
                vp++;
                v++;

            }
        }
        //extra cuts remained in horizontal 
        while(h<costhor.length){
            cost += (costhor[h]*vp);
            hp++;
            h++;
        }
        //extra cuts remained in vertical
        while(v<costver.length){
            cost += (costver[v]*hp);
            vp++;
            v++;
        }
        System.out.println(cost);
    }
    
}
