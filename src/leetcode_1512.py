from typing import List
from math import comb

class Solution:
    '''Given an array of integers nums, return the number of good pairs.

        A pair (i, j) is called good if nums[i] == nums[j] and i < j.
        
        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
        

        Input: nums = [1,1,1,1]
        Output: 6
        Explanation: Each pair in the array are good.
        
        Input: nums = [1,2,3]
        Output: 0

        '''
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashTable = {}
        sum = 0
        # last = nums[0]

        # for i in range(0,len(nums)):
        #     if nums[i] not in hashTable:
        #         hashTable[nums[i]] = 1
        #     else:
        #         hashTable[nums[i]] +=1
        #     if last != nums[i]:
        #         sum = sum + comb(hashTable[nums[i]],2)
        #     else:
        #         sum = hashTable[nums[i]]
        
        # return sum

        for num in nums:
            if num in hashTable:
                sum += hashTable[num]
                hashTable[num] +=1
            else:
                hashTable[num] = 1
        
        return sum