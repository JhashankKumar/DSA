package Numbers.Java;

public class AddFractions {
    public static void main(String[] args) {
        int numerator1 = 1;
        int denominator1 = 2;
        int numerator2 = 1;
        int denominator2 = 3;
        int resultNumerator = (numerator1 * denominator2) + (numerator2 * denominator1);
        int resultDenominator = denominator1 * denominator2;
        System.out.println("Result of adding " + numerator1 + "/" + denominator1 + " and " + numerator2 + "/" + denominator2 + " is: " + resultNumerator + "/" + resultDenominator);
    }
}
