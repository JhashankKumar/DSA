package RecursionBasics;
/*it gives frist occurance of key value in an array */
//it gives output as index value 
public class frist_occurance {
    public static int fristOccur(int arr[],int key,int i){
        if(i==arr.length){ /*checks wether it's end of array or not. if it is end of array then it return -1 as key was not found in array*/
            return -1;
        }
        if(arr[i]==key){ /*if key was found then it returns the index value of that key*/
            return i;
        }
        return fristOccur(arr, key, i+1); /*recursion*/
    }
    public static void main(String[] args) {
        int arr[]={2,3,4,6,7,8,9,12,54};
        System.out.println(fristOccur(arr, 3, 0));
        System.out.println(fristOccur(arr, 19, 0));
    }
    
}
