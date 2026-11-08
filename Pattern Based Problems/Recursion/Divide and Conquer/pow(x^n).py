# Findig Pow(x^n) using Divide and Conquer approach
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""

"""
Approach: Use Divide and Conquer
1. If n is 0, return 1 (base case).
2. If n is negative, return 1 / pow(x, -n) to handle negative exponents.
3. If n is even, calculate pow(x, n/2) and return the square of that result.
4. If n is odd, calculate pow(x, n-1) and multiply the result by x.
5. This approach reduces the number of multiplications needed, making it more efficient than the linear recursive approach.
"""

def pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0  # Base case: x^0 = 1
    elif n < 0:
        return 1 / pow(x, -n)  # For negative n, take the reciprocal of x^-n
    elif n % 2 == 0:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow  # If n is even, return (x^(n/2))^2
    else:
        return x * pow(x, n - 1)  # If n is odd, return x * x^(n-1)

if __name__ == "__main__":
    x1, n1 = 2.0, 10
    print(f"{x1}^{n1} = {pow(x1, n1)}")  # Output: 1024.0

    x2, n2 = 2.1, 3
    print(f"{x2}^{n2} = {pow(x2, n2)}")  # Output: 9.261

    x3, n3 = 2.0, -2
    print(f"{x3}^{n3} = {pow(x3, n3)}")  # Output: 0.25