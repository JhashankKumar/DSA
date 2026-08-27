public class Uppercase {
    public static String uppercase(String str){
        StringBuilder sb = new StringBuilder("");
        char ch=Character.toUpperCase(str.charAt(0)); //frist letter uppercasing
        sb.append(ch); //upper case letter 
        for(int i=1;i<str.length();i++){ //for finding space in a line
            if(str.charAt(i)==' '&&i<str.length()-1){ // if space found appending it and making uppercase letter next to space
                sb.append(str.charAt(i));
                i++;
                sb.append(Character.toUpperCase(str.charAt(i)));
            }
            else{  //if space not found appending character as it ease
                sb.append(str.charAt(i));
            }
        }
        return sb.toString(); // returning the string
    }
    public static void main(String[] args) {
        String str = "hi i am jhashank";
        System.out.println(uppercase(str)); // Output: "Hi I Am Jhashank"
    }
    
}
