# Top K Frequent Elements
"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:
Input: nums = [1], k = 1

Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

"""
Approach: HashMap and Frequency Counting
1. Use a hash map to count the frequency of each element in the array.
2. Create a list of unique elements from the hash map.
3. Sort the list of unique elements based on their frequency in descending order.
4. Return the first k elements from the sorted list as the result.

Time Complexity: O(n log n) due to sorting, where n is the number of unique elements in the array.
Space Complexity: O(n) for the hash map and the list of unique elements.
"""
def top_k_frequent_hashmap(nums, k):
    from collections import Counter

    # Step 1: Count the frequency of each element using a hash map
    frequency_map = Counter(nums)

    # Step 2: Create a list of unique elements
    unique_elements = list(frequency_map.keys())
    print(unique_elements)

    # Step 3: Sort the unique elements based on their frequency in descending order
    unique_elements.sort(key=lambda x: frequency_map[x], reverse=True)

    # Step 4: Return the first k elements from the sorted list
    return unique_elements[:k]

"""
Alternative Approach: Using a Min-Heap (Priority Queue)
1. Use a hash map to count the frequency of each element in the array.
2. Use a min-heap to keep track of the top k frequent elements.
3. Iterate through the frequency map and push elements into the min-heap.
4. If the size of the min-heap exceeds k, pop the smallest element from the heap.
5. After processing all elements, the min-heap will contain the k most frequent elements.
6. Return the elements in the min-heap as the result.
"""

def top_k_frequent_min_heap(nums, k):
    from collections import Counter
    import heapq

    # Step 1: Count the frequency of each element using a hash map
    frequency_map = Counter(nums)

    # Step 2: Use a min-heap to keep track of the top k frequent elements
    min_heap = []

    # Step 3: Iterate through the frequency map and push elements into the min-heap
    for num, freq in frequency_map.items():
        heapq.heappush(min_heap, (freq, num))
        print(min_heap)  # Debug: Print the current state of the min-heap
        # Step 4: If the size of the min-heap exceeds k, pop the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 5: Extract the elements from the min-heap
    result = [num for freq, num in min_heap]

    return result

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(top_k_frequent_hashmap(nums1, k1))  # Output: [1, 2]
    print(top_k_frequent_min_heap(nums1, k1))  # Output: [1, 2]

    nums2 = [1]
    k2 = 1
    print(top_k_frequent_hashmap(nums2, k2))  # Output: [1]
    print(top_k_frequent_min_heap(nums2, k2))  # Output: [1]

    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    print(top_k_frequent_hashmap(nums3, k3))  # Output: [1, 2]
    print(top_k_frequent_min_heap(nums3, k3))  # Output: [1, 2]
