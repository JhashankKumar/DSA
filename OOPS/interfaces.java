public class interfaces {
    public static void main(String[] args) {
        Queen q = new Queen();
        q.moves(); // it prints moves of queen
    }
    
}
interface ChessPlayer{ // interface
    void moves();
}
class Queen implements ChessPlayer{
    public void moves(){
        System.out.println("up,down,left,right,diagonal(in all 4 directions)");
    }
}
class Rook implements ChessPlayer{
    public void moves(){
        System.out.println("up,down,left,right");
    }
}