package Java;
/*
You are given an array ARR which has N integers. You want to construct a new array RES using ARR 
by following the below algorithm:
1. Initially, RES is empty
2. Start at any index of ARR
3. Choose a direction(left or right and iterate over the elements of ARR starting from the chosen 
index in the chosen direction
4. Add each iteration element to the end of the RES Additionally, it is given that the array ARR is cyclic.
 This means that after the last element you will iterate to the first one and vice versa. The value of RES 
 is the sum of the bitwise XOR value of all the prefixes of it. That means that the value of RES can be 
 defined as follows:
 value(RES) =RES[0] + (RES[0]^RES[1]) + (RES[0]^RES[1]^RES[2]) + ...............+ (RES[0]^RES[1]^RES[2]...... ^RES[N-1])
Find the maximum possible value of RES.
*/
/*
Example:
↓
I/P: N = 10 ARR = [7855922016]
rotate the array in right direction in a particular way to get the maximum value of RES
O/P: 99
considering RES =
value(RES) = 5 + (5^8) +*(5^8^7)+.........
value(RES) = 5+13+10+12+13+13+15+13+4+1
*/
public class XorSumInCircularArray {
    public static long maxXorSum(int[] arr) {
        int n = arr.length;
        long maxRes = 0;

        // // Calculate the XOR of all elements in the array
        // long totalXor = 0;
        // for (int num : arr) {
        //     totalXor ^= num;
        // }

        // Calculate the XOR of prefixes and update maxRes
        long prefixXor = 0;
        for (int i = 0; i < n; i++) {
            prefixXor ^= arr[i];
            maxRes += prefixXor;
        }

        // Consider the circular nature of the array
        for (int i = 0; i < n; i++) {
            prefixXor ^= arr[i]; // Remove the current element from prefixXor
            maxRes += prefixXor; // Add the new prefixXor to maxRes
        }

        return maxRes;
    }

    public static void main(String[] args) {
        int[] arr = {7,8,5,5,9,2,2,0,1,6};
        System.out.println(maxXorSum(arr)); // Output: 99
    }   
    
}
