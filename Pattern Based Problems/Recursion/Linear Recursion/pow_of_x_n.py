# Pow(x,n) find x raised to the power n
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
Approach:
1. We can solve the problem using a recursive approach.
2. The base case is when n is 0, in which case the result is 1.
3. For n > 0, we can find the result by recursively calling the function with n-1 and multiplying the result by x.
4. For n < 0, we can find the result by recursively calling the function with -n and taking the reciprocal of the result.
5. The final result can be obtained by returning the result of the recursive call.
"""

def pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0  # Base case: x^0 = 1
    elif n < 0:
        return 1 / pow(x, -n)  # For negative n, take the reciprocal of x^-n
    else:
        return x * pow(x, n - 1)  # Recursive case: x^n = x * x^(n-1)

if __name__ == "__main__":
    x1, n1 = 2.0, 10
    print(f"{x1}^{n1} = {pow(x1, n1)}")  # Output: 1024.0

    x2, n2 = 2.1, 3
    print(f"{x2}^{n2} = {pow(x2, n2)}")  # Output: 9.261

    x3, n3 = 2.0, -2
    print(f"{x3}^{n3} = {pow(x3, n3)}")  # Output: 0.25