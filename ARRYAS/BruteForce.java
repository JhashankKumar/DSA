public class BruteForce{
    public static void subarray(int numbers[]){
        int current_sum=0;
        int max_sum=Integer.MIN_VALUE;
        int min_sum=Integer.MAX_VALUE;
        for(int i=0;i<numbers.length;i++){ //it gives index of fist number in array
            int start=i;
            for(int j=i;j<numbers.length;j++){ // it gives index of second number to last number in array
                int end = j;
                current_sum=0; // after every subarray intialize the current_sum to zero
                for(int k=start;k<=end;k++){
                    System.out.print(numbers[k]+" "); // print the subarray
                    current_sum += numbers[k]; //calculates the sum of every subarray
                }
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
    

