public class kadanesalgo {
    public static void kadanes(int numbers[]){
        int max_sum=Integer.MIN_VALUE;
        int current_sum=0;
        for(int i=0;i<numbers.length;i++){
            current_sum += numbers[i];
            if(current_sum<0){
                current_sum=0;
            }
            max_sum=Math.max(current_sum,max_sum);
        }
        System.out.println("our max subarray sum is:"+max_sum);
    }
    public static void main(String[] args) {
        int numbers[]={1,3,5,7,9,11};
        kadanes(numbers);
       
    }
}
