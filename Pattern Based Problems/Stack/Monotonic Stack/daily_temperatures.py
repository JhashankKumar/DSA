# Daily Temperatures
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

"""
Approach: Stack based solution
1. Use a stack to keep track of indices of temperatures for which we haven't found a warmer day yet.
2. Iterate through the temperatures array.
3. For each temperature, while the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack, pop indices from the stack and update their corresponding result values.
4. Push the current index onto the stack.
5. Return the result array.
"""

def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # Initialize the result list with 0
    stack = []  # Stack to keep track of indices

    for i in range(n):
        # While stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()  # Pop the index from the stack
            result[index] = i - index  # Update the result for that index with the number of days waited

        stack.append(i)  # Push the current index onto the stack

    return result

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

    temperatures = [30, 40, 50, 60]
    print(daily_temperatures(temperatures))  # Output: [1, 1, 1, 0]

    temperatures = [30, 60, 90]
    print(daily_temperatures(temperatures))  # Output: [1, 1, 0]

