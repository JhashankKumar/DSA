//Job sequencing problem
/*
Given two arrays, deadline[] and profit[], where deadline[i] is the last time unit by which the 
i-th job must be completed, and profit[i] is the profit earned from completing it.
Each job takes 1 unit time, and only one job can be scheduled at a time. A job earns profit 
only if finished within its deadline. Find the number of jobs completed and maximum profit.

Examples: 

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job 1 (profit 20, deadline 4) can be scheduled. Among the three jobs with deadline 1, 
only one fits, so we pick the highest profit (40). Hence, 2 jobs with total profit = 60.

Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Picking the job with profit 100 (deadline 2) and the job with profit 27 (deadline 2); 
they can occupy the two available slots before deadline 2. Thus 2 jobs are scheduled for a maximum
total profit of 127.
*/

import java.util.*;
public class jobSequence {
    static class Job{
        int deadline;
        int profit;
        int id;
        public Job(int i,int d, int p){
            id=i;
            deadline=d;
            profit=p;
        }
    }
    public static void main(String[] args) {
        int jobInfo[][]={{4,20},{1,10},{1,40},{1,30}};

        ArrayList<Job> jobs = new ArrayList<>();

        for(int i=0;i<jobInfo.length;i++){
            jobs.add(new Job(i,jobInfo[i][0],jobInfo[i][1]));
        }

        Collections.sort(jobs,(obj1,obj2)->obj2.profit-obj1.profit);
        //decending order of profit
        //for ascending order obj1 and obj2 places shifted
        ArrayList<Integer> seq = new ArrayList<>();
        int time = 0;
        for(int i=0;i<jobs.size();i++){
            Job curr = jobs.get(i);
            if(curr.deadline>time){
                seq.add(curr.id);
                time++;

            }
        }
        //print seq
        System.out.println("max jobs="+seq.size());
        for(int i=0;i<seq.size();i++){
            System.out.println(seq.get(i)+" ");
        }
        System.out.println();
    }
}
