public class bit_operations {
    public static int getithbit(int n ,int i){
        int bitmask = 1<<i;
        if((n & bitmask) == 0){
            return 0;
        }
        else{
            return 1;
        }
    }
    public static int setithbit(int n , int i){
        int bitmask = 1<<i;
        return n|bitmask;
    }
    public static int clearithbit(int n ,int i){
        int bitmask = ~(1<<i);
        return n&bitmask;
    }
    public static int updateithbit(int n, int i,int newbit){
        if(newbit == 0){
            return clearithbit(n,i);
        }
        else{
            return setithbit( n,i);
        }
        // another process
        // n = clearithbit(n,i);
        // int bitmask = newbit<<i;
        // return n|bitmask;
    }
    public static int clearlast_i_bits(int n, int i){
        int bitmask = (~0)<<i;
        return n & bitmask;
    }
    public static int clearbits(int n ,int i, int j){
        int a = ((~0)<<(j+1));
        int b = (1<<i)-1;
        int bitmask = a|b;
        return n & bitmask;
    }
    public static boolean ispoweroftwo(int n){
        return(n&(n-1))==0;
    }
    public static int countsetbits(int n){
        int count = 0 ;
        while(n>0){
            if((n & 1) !=0){
                //check our LSB
                count ++;
            }
             n = n >> 1;
        }
        return count;
    }
    public static void main(String[] args) {
        System.out.println(getithbit(10, 3));
        System.out.println(setithbit(10, 2));
        System.out.println(updateithbit(10, 2, 1));
        System.out.println(clearlast_i_bits(15, 2));
        System.out.println(clearbits(10, 2, 4));
        System.out.println(ispoweroftwo(16));
        System.out.println(countsetbits(15));
    }
    
}
