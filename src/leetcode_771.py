class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        # This solution is O(n^2) because lookup in a string is O(n)
        # for stone in stones:
        #     if stone in jewels:
        #         counter +=1
        
        # return counter

        # This solution is O(n+m), where n is length of stones, and m is lenght of jewels
        jewelTable = {}
    
        for jewel in jewels:
            jewelTable[jewel] = True
        
        for stone in stones:
            if stone in jewelTable:
                counter += 1
        
        return counter