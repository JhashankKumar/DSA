import java.util.*;
public class Coins {
    public static void main(String[] args) {
        Integer coins[]={1, 2, 5, 10, 20, 50, 100, 2000};
        // Arrays.sort(coins,Comparator.reverseOrder());
        // Arrays.sort(coins,Collections.reverseOrder());
        int amount = 590;
        whileLoop(coins, amount);
    }

    public static void whileLoop(Integer coins[], int amount){
        // coins should be in decending order sort 
        Arrays.sort(coins,Collections.reverseOrder());
        int countOfCoins = 0;
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

    public static void usingMath(Integer coins[], int amount){
        // coins should be in decending order sort 
        Arrays.sort(coins,Collections.reverseOrder());
        int countOfCoins = 0;
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=0;i<coins.length;i++){
            if(coins[i]<=amount){
                int numOfCoins = amount/coins[i];
                countOfCoins+=numOfCoins;
                for(int j=0;j<numOfCoins;j++){
                    ans.add(coins[i]);
                }
                // amount-=numOfCoins*coins[i];
                amount%=coins[i];
            }
        }
        System.out.println(countOfCoins+" ");
        for(int i=0;i<ans.size();i++){
            System.out.println(ans.get(i)+" ");
        }
        System.out.println();
    }
    
}
