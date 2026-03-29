public class NQueens {
    //isSafe function will check wether the Q position is perfectly set or not 
    //for this vizualization by placing Q in the center square
    public static boolean isSafe(char board[][],int row,int col){
        //vertical up
        for(int i=row-1;i>=0;i--){
            if(board[i][col]=='Q'){
                return false;
            }
        }
        //diagonal right up
        for(int i=row-1,j=col+1;i>=0&&j<board.length;i--,j++){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        //diagonal left up
        for(int i=row-1,j=col-1;i>=0&&j>=0;i--,j--){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
    //this function is for printing all possible ways
    public static void Nqueen(char board[][],int row){
       //base case
        if(row==board.length){
        //printBoard(board);//it prints all possible ways
        count++;//it counts all possible ways[it is optimum code]
        return;
        }
       //column loop
        for(int j=0;j<board.length;j++){
            if(isSafe(board,row,j)){//condition
                board[row][j]='Q';
                Nqueen(board,row+1);//function recursive call
                board[row][j]='x';//bacl tracking
            }
        }   
    }
    //this funtion is for printing only one possible way
    public static boolean NQueen(char board[][],int row){
        //base
        if(row ==board.length){
            return true;
        }
        //column loop
        for(int j=0;j<board.length;j++){
            if(isSafe(board,row,j)){
                board[row][j]='Q';
                if(NQueen(board, row+1)){
                    return true;
                }
                board[row][j] ='x';
            }
        }
        return false;

    }
    public static void printBoard(char baord[][]){
        System.out.println("-----CHESS BOARD-----");
        for(int i=0;i<baord.length;i++){
            for(int j=0;j<baord[0].length;j++){
                System.out.print(baord[i][j]+" ");
            }
            System.out.println();
        }
    }
    static int count = 0;//for optimal code 
    public static void main(String[] args) {
        int n=4;
        char board[][]=new char[n][n];
        //initialize board with "."
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j]='x';
            }
        }
        //below if condition will check and prints solution is possible or not
        if(NQueen(board,0)){
            System.out.println("solution is possible");
            printBoard(board);
        }
        else{
            System.out.println("solution is not possible");
        }
        Nqueen(board,0);//it prints all possible solutions
        NQueen(board,0);//it prints only single solution if solution possible

        System.out.println(count);
    }
}
