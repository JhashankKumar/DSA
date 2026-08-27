public class diagonalsum1 {
    public static int diagonalsum(int matrix[][]){
      int sum=0;
      for(int i=0;i<=matrix.length-1;i++){
        for(int j=0;j<=matrix[0].length-1;j++){
            if(i==j){
                sum += matrix[i][j];
            }
            else if(i+j==matrix.length-1){
                if(i!=j){
                    sum += matrix[i][j];
                }
            }

        }
       
      }  
      return sum ;

    } 
    public static void main(String[] args) {
        int matrix[][]={{1,2,3},{4,5,6},{7,8,9}};
        int sum= diagonalsum(matrix);
        System.out.println(sum);
    }
}
