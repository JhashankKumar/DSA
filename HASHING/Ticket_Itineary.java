import java.util.*;

public class Ticket_Itineary {
    public static String getstart(HashMap<String,String> tickets){
        HashMap<String,String> revMap = new HashMap<>();
        for(String key: tickets.keySet()){
            revMap.put(tickets.get(key), key);
        }
        for(String key: tickets.keySet()){
            if(!revMap.containsKey(key)){
                return key; // starting point
            }
        }
        return null;//starting point not exist
    }
    public static void main(String[] args) {
        HashMap<String,String> tickets = new HashMap<>();
        tickets.put("Chennai", "Benguluru");
        tickets.put("Mumbai", "Delhi");
        tickets.put("Goa", "Chennai");
        tickets.put("Delhi", "Goa");   

        String start = getstart(tickets);
        System.out.print(start);
        for(String key : tickets.keySet()){
            System.out.print("->"+tickets.get(start));
            start = tickets.get(start);
        }
        System.out.println();
    }
    
}
