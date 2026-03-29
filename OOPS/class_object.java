// class is a blue print of object
public class class_object {
public static void main(String[] args) {
    Pen p1 = new Pen(); // created a pen object called p1
    System.out.println(p1.getColor());
    p1.setTip(5); // defining new object attribute
    System.out.println(p1.getTip());
    p1.setColor("blue"); // defining new object attribute
    System.out.println(p1.getColor());

    BankAccount myAcc = new BankAccount();
    myAcc.username ="JhashankKumar";
    myAcc.setpassword("jack123@$ardar");
}
// user defined classes and blue prints   
}
//Bank Account blueprint
class BankAccount{
    public String username;
    public void setpassword(String pwd){
    }
}
// blue print of pen
class Pen{ // class 
    private String color; // attribute (properties)
    private int tip; // attribute
    String getColor(){ // getters
        return this.color;
    }
    int getTip(){ // getters 
        return this.tip;
    }
    void setColor(String newColor){ // funtions , sitters
        color = newColor;
    }
    void setTip(int newTip){ // functions , sitters
        tip = newTip;
    }
}
