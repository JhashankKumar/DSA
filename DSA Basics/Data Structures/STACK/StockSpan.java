
import java.util.*;

public class StockSpan {
    public static void stockspan(int stock[],int span[]){
        Stack<Integer> s = new Stack<>();
        //initalizing frist day as 1 because pervious day cannot be knowm
        span[0] = 1;
        s.push(0);
        //method to find span of current day 
        for(int i=1;i<stock.length;i++){
            int currprice = stock[i];
            while(!s.isEmpty()&&currprice > stock[s.peek()]){
                s.pop();
            }
            //if all values in stack are poped means the frist day value and last day value are equal
            //then in span i+1 value is stored in i th index
            //else previous index is finded out and difference is stored in span i th index
            if(s.isEmpty()){
                span[i] = i+1;
            }else{
                int prevHigh = s.peek();
                span[i] = i - prevHigh;
            }
            s.push(i);
        }
    }
    public static void main(String[] args) {
        int stock[] = { 100, 80, 60, 70, 60, 85, 100};
        int span[] = new int[stock.length];
        stockspan(stock, span);
        
        for(int i=0; i<span.length;i++){
            System.out.println(span[i]+" ");
        }

    }
}
