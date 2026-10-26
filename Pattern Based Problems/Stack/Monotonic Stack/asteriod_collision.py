# Astroid Collision Problem
"""
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.


Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.
 
Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

"""
Approach: Stack based solution
1. Create a stack to keep track of the asteroids that are still in motion.
2. Iterate through the asteroids array.
3. For each asteroid, check if it is moving left (negative) and if the top of the stack is moving right (positive). If so, a collision occurs.
4. Compare the sizes of the colliding asteroids:
   a. If the current asteroid is larger, pop the top of the stack and continue checking for further collisions.
   b. If the current asteroid is smaller, it explodes and we break out of the loop.
   c. If they are the same size, both explode and we pop the top of the stack and break out of the loop.
5. If the current asteroid survives all collisions, push it onto the stack.
6. Return the stack as the final state of the asteroids.
"""

def asteroid_collision(asteroids):
    stack = []  # Stack to keep track of asteroids

    for asteroid in asteroids:
        # Check for collision: current asteroid is moving left and top of stack is moving right
        while stack and asteroid < 0 < stack[-1]:
            if abs(asteroid) > stack[-1]:  # Current asteroid is larger
                stack.pop()  # Pop the top of the stack (it explodes)
                continue  # Continue checking for further collisions
            elif abs(asteroid) == stack[-1]:  # Both are the same size
                stack.pop()  # Both explode
            break  # Current asteroid explodes or both explode, break out of the loop
        else:
            stack.append(asteroid)  # No collision, push current asteroid onto the stack

    return stack

if __name__ == "__main__":
    asteroids = [5, 10, -5]
    print(asteroid_collision(asteroids))  # Output: [5, 10]

    asteroids = [8, -8]
    print(asteroid_collision(asteroids))  # Output: []

    asteroids = [10, 2, -5]
    print(asteroid_collision(asteroids))  # Output: [10]

    asteroids = [3, 5, -6, 2, -1, 4]
    print(asteroid_collision(asteroids))  # Output: [-6, 2, 4]