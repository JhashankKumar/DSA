public class static_keywords {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.getName();
        s1.schoolName = "jvm";
        Student s2 = new Student();
        s2.name = "jack";
        System.out.println(s2.schoolName);
    }
}
class Student {
    String name;
    int roll;

    String schoolName;

    void setName(String name){
        this.name = name;
    }
    String getName(){
        return this.name;
    }
}