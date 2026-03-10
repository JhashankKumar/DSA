// import java.io.*;

// public class ReverseBits {
//     //use long for n-bit integers
//     public static void main(String[] args) throws Exception {
//         BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//         long input = Long.parseLong(reader.readLine());
//         long output = reverseBits(input);
//         System.out.println("Original Integer: " + input);
//         System.out.println("Reversed Bits Integer: " + output);
//     }

//     private static long reverseBits(long integer) {
//         long reversed = 0;
//         for (int i = 0; i < 64; i++) {
//             reversed <<= 1; // Shift left to make room for the next bit
//             reversed |= (integer & 1); // Add the least significant bit of integer to reversed
//             integer >>= 1; // Shift integer right to process the next bit
//         }
       
//     }
// }
// didn't got correct input and output, need to check the logic of reversing bits and also the input format for long integers.