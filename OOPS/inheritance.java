public class inheritance {
    public static void main(String[] args) {
        //Fish shark = new Fish();
        //shark.eat();
        // Dog dobby = new Dog();
        // dobby.eat();
        // dobby.legs = 4;
        // System.out.println(dobby.legs);
    }
    
}
// base class
class Animal{
    String color;
    void eat(){
        System.out.println("eats");
    }
    void breathe(){
        System.out.println("breathes");
    }
}
//derived class (single level inheritance)
// class Fish extends Animal{
//     int fins;
//     void swim(){
//         System.out.println("swims in water");
//     }
// }

//multi level inheritance
// class Mammal extends Animal{
//     int legs;
// }
// class Dog extends Mammal {
//     String bread;
// }
//hierarchial inheritance
class Mammal extends Animal{
    void walk(){
        System.out.println("walk");
    }
}
class Bird extends Animal{
    void fly(){
        System.out.println("fly");
    }
}
class Fish extends Animal{
    void swim(){
        System.out.println("swim");
    }
}
