# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Approach 1: Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # nums_set = set()
    # for num in nums:
    #     if num in nums_set:
    #         return num
    #     else:
    #         nums_set.add(num)

    # Approach 2: Floyd Cycle Detection
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow