public class fruit_polymorph {
    public static void main(String[] args) {
        Grape a = new Grape();
        a.fruit();

        
    }
    
}
class Fruit{
    void fruit(){
        System.out.println("i am fruit");
    }
}
class Grape extends Fruit{
 
}
class Banana extends Fruit{
    void fruit(){
        System.out.println("i am banana");
    }
}
