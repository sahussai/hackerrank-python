class Solution:
    '''
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.


    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    '''
    @classmethod
    def isPalindrome(cls, x: int) -> bool:
        
        strNum = str(x)
        length = len(strNum)
        
        maxIter = length // 2

        for i in range(maxIter):
            if strNum[i] != strNum[length - i - 1]:
                return False
        
        return True