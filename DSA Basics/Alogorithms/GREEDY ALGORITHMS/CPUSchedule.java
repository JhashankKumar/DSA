import java.util.Arrays;
import java.util.Scanner;

public class CPUSchedule {
    public static void jobs(int[] priority, int[] end){
        int job[][] = new int[priority.length][2];
        for(int i=0;i<priority.length;i++){
            job[i][0] = priority[i];
            job[i][1] = end[i];
        }
        //if 1 is high priority
        // Arrays.sort(job, (a,b) -> Integer.compare(a[0],b[0]));
        //if 9 is high priority (decending )
        // Arrays.sort(job, (a,b) -> Integer.compare(b[0],a[0]));
        Arrays.sort(job,(a,b)->{
            if(a[0]==b[0]){
                return Integer.compare(b[1],a[1]);
            }            return Integer.compare(a[0],b[0]);
        });
        for(int i = 0;i<priority.length;i++){
            System.out.print(job[i][0]+" "+ job[i][1]+","+ " " );
        }
        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Tjobs = sc.nextInt();
        int priority[] = new int[Tjobs];
        int end[] = new int[Tjobs];
        for (int i = 0; i < Tjobs; i++) {
            priority[i] = sc.nextInt();
        }
        for (int i = 0; i < Tjobs; i++) {
            end[i] = sc.nextInt();
        }
        jobs(priority, end);
        sc.close();
    }
}
