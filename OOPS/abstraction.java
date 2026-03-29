/* in an abstract class or parent class we define a function (ex: walk) called abstract function, that function should be used in every child class .
that function implementation will change for every child class. 
*/
public class abstraction {
    public static void main(String[] args) {
       Horse h = new  Horse();
       h.eat();
       h.walk();
       h.changeColor();
       Chicken c= new Chicken();
       c.color();
       c.eat();
       c.walk();
    Mustang myhorse = new Mustang();
    System.out.println(myhorse);
    //hierarchy of calling class or constructor is Animal -> Horse -> Mustang 
    }
    
}
//abstraction came into existence as walk function implementation depends on derived classes [ex: horse , chicken]
//it does not depend on animal , so animal gives idea about walk that it present in every derived animal
//it gives that walk is void type and does not take parameters
abstract class Animal{ // parent class
    String color ;
    Animal(){ // constructor /*this constructor will assign this default color to every child class irrespective of object that has been creating */
        color = "brown";
        System.out.println("animal constructor is called ");
    }
    void eat(){ //non abstract method
        System.out.println(" animal eats");
    }
    //abstract method
    abstract void walk();
}
class Horse extends Animal{ // child class
    Horse(){ // constructor 
        System.out.println("horse constructor is called");
    }
    //traditional method
    void changeColor(){ // in order to change the default color assigned by constructor in child class we use a function
        color = "dark brown";
        System.out.println(color);
    }
    void walk(){
        System.out.println("walks on 4 legs");
    }
}
class Mustang extends Horse{
    Mustang(){ // constructor 
        System.out.println("mustang constructor is called");
    }
}    
class Chicken extends Animal{ // child class
    void walk(){
        System.out.println("walks on 2 legs");
    }
}
