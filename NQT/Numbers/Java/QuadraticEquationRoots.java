package Numbers.Java;

public class QuadraticEquationRoots {
    public static void main(String[] args) {
        double a = 1; // Coefficient of x^2
        double b = -3; // Coefficient of x
        double c = 2; // Constant term

        double discriminant = b * b - 4 * a * c;

        if (discriminant > 0) {
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.println("The roots are real and distinct: " + root1 + " and " + root2);
        } else if (discriminant == 0) {
            double root = -b / (2 * a);
            System.out.println("The roots are real and equal: " + root);
        } else {
            System.out.println("The roots are complex and imaginary.");
        }
    }
}
