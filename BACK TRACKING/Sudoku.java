package BackTracking;

public class Sudoku {
    //this isSafe function checks wether the element placed in box is safe to place it there
    //that means it verify wether the value exist in that row or in that same column before only
    //if number already present then this function will return false 
    public static boolean isSafe(int sudoku[][],int row,int col,int digit){
        //column condition
        //it checks for wether column consist already the number that we want to place
        //if present returns false 
        for(int i=0;i<=8;i++){
            if(sudoku[i][col]==digit){
                return false;
            }
        }
        //row condition
        //it checks for wether row consist already the number that we want to place
        //if present returns false
        for(int j=0;j<=8;j++){
            if(sudoku[row][j]==digit){
                return false;
            }
        }
        //grid condition
        //it checks for wether grid consist already the number that we want to place
        //if present returns false
        int sr = (row/3)*3;
        int sc = (col/3)*3;
        //above two sc and sr will give grid starting address. In that grid only we store the  value 
        for(int i=sr;i<sr+3;i++){
            for(int j=sc;j<sc+3;j++){
                if(sudoku[i][j]==digit){
                    return false;
                }
            }
        }
        return true;
    }
    public static boolean sudokusolver(int sudoku[][],int row,int col){
        //base case
        if(row == 9){
            return true;
        }
        //recursion
        //if column in the row exceeds its limit then if condition will come into picture
        int nextRow = row ,nextCol = col+1;
        if(col+1 == 9){
            nextRow = row+1;
            nextCol = 0;
        }
        // this condition come into picture when a number present zero in the box or not 
        //it will check if zero not present in the box then it will again call the function for next column
        if(sudoku[row][col] != 0){
            return sudokusolver(sudoku, nextRow, nextCol);
        }
        //if zero present in the box then
        //this to check what number should placed in box 
        for(int digit =1 ; digit<=9;digit++){
            if(isSafe(sudoku,row,col,digit)){
                //if isSafe transfer true then the digit is placed in that box
                //else it transfer false to sudokuSolver and it checks for next number
                sudoku[row][col]=digit;
                //if the value placed in the box is fit then call for next box 
                if(sudokusolver(sudoku, nextRow, nextCol)){ // recursive function call
                    //if the value placed in the box is not existing in the row then it will pass true
                    return true;
                }
                sudoku[row][col] = 0;
            }
        }
        return false;
    }
    public static void printSudoku(int sudoku[][]){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                System.out.print(sudoku[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int sudoku[][]={{0, 0, 8, 0, 0, 0, 0, 0, 0, 0},
        {4, 9, 0, 1, 5, 7, 0, 0, 2},
        {0, 0, 3, 0, 0, 4, 1, 9, 0},
        {1, 8, 5, 0, 6, 0, 0, 2, 0},
        {0, 0, 0, 0, 2, 0, 0, 6, 0},
        {9, 6, 0, 4, 0, 5, 3, 0, 0},
        {0, 3, 0, 0, 7, 2, 0, 0, 4},
        {0, 4, 9, 0, 3, 0, 0, 5, 7},
        {8, 2, 7, 0, 0, 9, 0, 1, 3}};

        if(sudokusolver(sudoku, 0, 0)){
            System.out.println("solution exist");
            printSudoku(sudoku);
        }else{
            System.out.println("solution doesn't exist");
        }
        
    }
    
}
