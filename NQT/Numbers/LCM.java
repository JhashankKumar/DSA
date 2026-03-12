package Numbers;

public class LCM {
    public static void main(String[] args) {
        int num1 = 48;
        int num2 = 18;
        int lcm = findLCM(num1, num2);
        System.out.println("LCM of " + num1 + " and " + num2 + " is: " + lcm);  
    }

    private static int findLCM(int a, int b) {
        return (a * b) / findGCD(a, b);
    }

    private static int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a % b);
    }
}
