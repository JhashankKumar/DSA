import java.util.*;
public class Coins {
    public static void main(String[] args) {
        Integer coins[]={1, 2, 5, 10, 20, 50, 100, 2000};
        Arrays.sort(coins,Comparator.reverseOrder());
        
        int countOfCoins = 0;
        int amount = 500;
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=0;i<coins.length;i++){
            if(coins[i]<=amount){
                while(coins[i]<=amount){
                    countOfCoins++;
                    ans.add(coins[i]);
                    amount-=coins[i];
                }
            }
        }
        System.out.println(countOfCoins+" ");
        for(int i=0;i<ans.size();i++){
            System.out.println(ans.get(i)+" ");
        }
        System.out.println();
    }
}
