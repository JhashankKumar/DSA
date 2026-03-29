public class diagonalsumoptimum {
    public static int diagonalsum(int matrix[][]){
        int sum=0;
        for(int i=0;i<=matrix.length-1;i++){
            //primary diagonal
            sum += matrix[i][i];
            //secondary diagonal
            if(i!=matrix.length-i-1){
                sum += matrix[i][matrix.length-i-1];
            }
        }
        return sum;
    } 
    public static void main(String[] args) {
        int matrix[][]={{1,2,3},{4,5,6},{7,8,9}};
        int sum= diagonalsum(matrix);
        System.out.println(sum);
    }
}
