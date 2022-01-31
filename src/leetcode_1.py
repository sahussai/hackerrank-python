
class Solution:
    '''
    Leetcode 1: Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    
    Example
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    '''

    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        hTable = {}
        
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            hTable[compliment] = i 
        
        for x in range(0, len(nums)):
            if nums[x] in hTable and x != hTable[nums[x]]:
                return [x, hTable[nums[x]]]
        
        return []
        
        ## Brute force method

        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return[i,j]

        # return []

        
    




    '''
    
    Steps:
    Thoughts:
    Using abs will not work. There are negative numbers in the array.


    [2,7,11,15], target = 9
    1. Create a hashtable with all the entries. This is O(n)
        {
            2: 0
            7: 1
            11: 2
            15: 3
        }
    2. Loop through nums:
        if 2 - 9) is in hTable
            return [indexOf(2), hTable[abs(2-9)]] 


    What if the inputs are negative?
    [2,-7, ]

    
    '''

