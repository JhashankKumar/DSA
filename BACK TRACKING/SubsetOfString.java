package BackTracking;

public class SubsetOfString {
    public static void findSubSet(String str, int i,String ans){
        if(i == str.length()){
            if(ans.length()==0){
                System.out.println("null");
            }else{
                System.out.println(ans);
            }
            return;
        }
        findSubSet(str, i+1, ans+str.charAt(i));//yes
        findSubSet(str,i+1,ans);//no
    }
    public static void main(String[] args) {
        String alph="abc";
        findSubSet(alph,0, "");
    }

}
