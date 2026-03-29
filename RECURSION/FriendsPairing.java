package RecursionBasics;

public class FriendsPairing {
    public static int friendpair(int n){
        if(n==1||n==2){//base cases 
            return n;
        }
        //making choice 
        //single
        int fnm1=friendpair(n-1);
        //pair
        int fnm2 = friendpair(n-2);
        int pairways = (n-1)*fnm2;
        //totalways
        int totalways = fnm1+pairways;
        return totalways;
        //optimum way to write code for pairing friends is below
        //return friendpair(n-1)+(n-1)*friendpair(n-2);
    }
    public static void main(String[] args) {
        System.out.println(friendpair(4));
    }
    
}
