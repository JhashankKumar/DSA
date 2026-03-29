public class stringcomp_substr {
    public static void substring(String str,int si,int ei){
        String substr ="";
        for(int i=si;i<ei;i++){
            substr += str.charAt(i);
        }
        System.out.println(substr);
    }
    public static void main(String[] args) {
        String s1 ="tony";
        String s2 ="tony";
        String s3 = new String("tony");
        String s ="helloworld";
        //substring printing traditional 
        substring(s,0,5);
        //using substring function
        System.out.println(s.substring(0,5));

        //string interning occur in traditional comparision
        if(s1==s2){
            System.out.println("strings are equal");
        }
        else{
            System.out.println("strings are not equal");
        }
        if(s1==s3){
            System.out.println("strings are equal");
        }
        else{
            System.out.println("strings are not equal");
        }
        //compareTo function
        if(s1.equals(s3)){
            System.out.println("strings are equal");
        }
        else {
            System.out.println("strings are not equal");
        }
        

    }    
}
