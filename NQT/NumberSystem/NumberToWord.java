package NumberSystem;

public class NumberToWord {
    private static final String[] units = {
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    };
    private static final String[] tens = {
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };
    private static final String[] thousands = {
            "", "Thousand", "Million"
    };

    public static void main(String[] args) {
        //number can be upto millions, you can change this value to test with different numbers
        int number = 12345; // You can change this value to test with different numbers
        String wordValue = numberToWords(number);
        System.out.println("The word representation of number " + number + " is:  " + wordValue);
    }

    private static String numberToWords(int number) {
        if (number == 0) {
            return "Zero";
        }
        StringBuilder wordValue = new StringBuilder();
        int thousandCounter = 0;

        while (number > 0) {
            if (number % 1000 != 0) {
                wordValue.insert(0, convertLessThanThousand(number % 1000) + " " + thousands[thousandCounter] + " ");
            }
            number /= 1000;
            thousandCounter++;
        }
        return wordValue.toString().trim();
    }

    private static String convertLessThanThousand(int number) {
        StringBuilder word = new StringBuilder();
        if (number >= 100) {
            word.append(units[number / 100]).append(" Hundred ");
            number %= 100;
        }
        if (number >= 20) {
            word.append(tens[number / 10]).append(" ");
            number %= 10;
        }
        if (number > 0) {
            word.append(units[number]).append(" ");
        }
        return word.toString().trim();
    }

}
