/*constructors will contain the parameters which are needed to be defined in every object that been created */
public class constructor {
    public static void main(String[] args) {
        student s1 = new student();//constructor call 
        System.out.println(s1.name);
        s1.roll = 345;
        System.out.println(s1.roll);
        s1.password = "abcd";
        s1.marks[0]=100;
        s1.marks[1]=93;
        s1.marks[2]=88;
        //copy constructor example
        student s2 = new student(s1);
        s2.password = "xyz";
        s1.marks[2]=100;
        for (int i=0;i<=3;i++){
            System.out.println(s2.marks[i]);
        }
    }
    
}
class student{
    String name;
    int roll;
    String password;
    int marks[];
    public String schoolName;
    //when a student forgets his password we need to create a new object with old data
    // shallow copy constructor
    // void Student(student s1) {
    //     marks = new int [3];
    //     this.name = s1.name;
    //     this.roll = s1.roll;
    //     this.marks = s1.marks;
    //  }
    // deep copy constuctor 
    void Student(student s1) {
        marks = new int [3];
        this.name = s1.name;
        this.roll = s1.roll;
        for (int i=0;i<=marks.length;i++){
            this.marks[i]=s1.marks[i];
        }
     }

    student(student s1){ // parameterized constructor
        marks = new int [3];
        this.name = s1.name;
        this.roll = s1.roll;
        this.marks = s1.marks;
    }
    student(){ // non parameterized constructor
        marks = new int [3];
        System.out.println("constructor is called");
    }
    student(int roll){ // parameterized constructor
        marks = new int [3];
        this.roll = roll;
    }
}
