package RecursionBasics;
public class duplicate_remove {
    public static void RemoveDuplicates(String str , int idx , StringBuilder newstr, boolean map[]){
        if(idx == str.length()){ // checking the length of the given string completed or not
            System.out.println(newstr);
        }
        //work
        /*checking each character and checking wether it was present in map or not  */
        char currchar = str.charAt(idx);
        if(map[currchar-'a']==true){
            //duplicate
            //if charecter value is true then present valu is duplicate then that value is not stored in new string and go to next index
            RemoveDuplicates(str, idx+1, newstr, map);
        }
        else{
            //the current charecter is appearing frist time 
            //so it was appended into new string 
            map[currchar-'a']=true;
            RemoveDuplicates(str, idx+1, newstr.append(currchar), map);
        }
    }
    public static void main(String[] args) {
        String str = "jhashankkumar";
        RemoveDuplicates(str,0,new StringBuilder(""),new boolean[26]);
        //new string was created using StringBuilder and boolean map was created using boolean 
    }
    
}
