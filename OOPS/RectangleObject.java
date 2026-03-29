import java.util.Scanner;

public class RectangleObject { //main class
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //object1 created
        Rectangle room1 = new Rectangle();//non-parameterized constructor is used 
        room1.setlength(45);
        room1.setwidth(20);
        System.out.println(room1.calculateArea());
        System.out.println(room1.calculatePerimeter());
        //object2 created
        Rectangle room2 = new Rectangle(50,26);//parameterized constructor is used 
        System.out.println(room2.calculateArea());
        //creating two objects with parameterized constructor
        // Rectangle Kitchen = new Rectangle(50,26);
        // Rectangle Bedroom = new Rectangle(100,50);
        //calling CalculateTotalArea method
        //object value initalized with method
        Rectangle kitchen = getroom();
        Rectangle Bedroom = getroom();

        double area = CalculateTotalArea(kitchen , Bedroom);
        System.out.println("total area ="+area);
        sc.close();
    }
    //creating a method which takes parameters from objects and return area
    //objects as method parameter
    public static double CalculateTotalArea(Rectangle rectangle1,Rectangle rectangle2){
        return rectangle1.calculateArea()+rectangle2.calculateArea();
    }
    //objects as method return type
    /*In java a method can return only one value to main function when it is called.
    for multiple value return we use object as method return type*/ 
    public static Rectangle getroom(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length of your room");
        double length = sc.nextDouble();

        System.out.println("Enter the width of your room ");
        double width = sc.nextDouble(); 
        sc.close();

        return new Rectangle(length, width);
    }

}
class Rectangle{ //class (blue print of object)
    private double length;//attributes 
    private double width;//attributes
    public Rectangle(){ //non-parameterized constructor
        length = 0;
        width = 0;
    }
    public Rectangle(double length, double width){//parameterized constructor
        setlength(length);
        setwidth(width);

    }
    public double calculatePerimeter(){//functions
        return (2*length)+(2*width);
    }
    public double calculateArea(){//function
        return length*width;
    }
    //getters
    public double getlength(){
        return length;
    }
    public double getwidth(){
        return width;
    }
    //setters
    public void setlength(double length){
        this.length = length;
    }
    public void setwidth(double width){
        this.width = width;
    }

}