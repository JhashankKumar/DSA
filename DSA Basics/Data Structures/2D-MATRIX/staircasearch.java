public class staircasearch {
    public static boolean staircase(int matrix[][],int key){
        int row=0,column=matrix[0].length-1;
        while(row < matrix.length && column>=0){
            if(matrix[row][column]==key){
                System.out.println("found key at (" + row +","+column+")");
                return true;
            }
            else if(key < matrix[row][column]){
                column--;
            }
            else{
                row++;
            }
        }
        System.out.println("key not found");
        return false;
    }
    public static void main(String[] args) {
        int matrix[][]={{}};
        staircase(matrix, 33);
        
    }

    
}