public class PrefixSum {
    public static void subarray(int numbers[]){
        int current_sum=0;
        int max_sum=Integer.MIN_VALUE;
        int min_sum=Integer.MAX_VALUE;
        int prefix[]=new int[numbers.length];
        //prefix array calculation
        prefix[0]=numbers[0];
        for(int i=1;i<prefix.length;i++){
            prefix[i]=prefix[i-1]+numbers[i];
        }
        for(int i=0;i<numbers.length;i++){ //it gives index of fist number in array
            int start=i;
            for(int j=i;j<numbers.length;j++){ // it gives index of second number to last number in array
                int end = j;
                current_sum=0; // after every subarray intialize the current_sum to zero
                current_sum= start==0 ? prefix[end] : prefix[end]-prefix[start-1];
                System.out.println();
                System.out.println("sum of subarray="+current_sum); // print the sum of subarray
                if(max_sum<current_sum){ //checking for max sum of subarray
                    max_sum = current_sum;
                }
                if(min_sum>current_sum){ // checking for min sum of subarray
                    min_sum = current_sum;
                }
            }
        }
        System.out.println(" max sum = "+max_sum);
        System.out.println("min sum ="+min_sum);

       
    }
    public static void main(String[] args) {
        int numbers[]={1,3,5,7,9,11};
        subarray(numbers);
       
    }
}
