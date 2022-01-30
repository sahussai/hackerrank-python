from leetcode_1512 import Solution as lc_1512
from leetcode_771 import Solution as lc_771
from leetcode_1365 import Solution as lc_1365
from bubbleSort import BubbleSort
from binarySearch import BinarySearch



''' Leetcode 1512 Number of Good Pairs'''
# array = [1,2,3,1,1,3]
# array2 = [1,1,1,1]
# print(lc_1512.numIdenticalPairs(array,array))


''' Leetcode 771 Jewels and Stones'''
# jewels = "aA"
# stones = "aAAbbbAAa"

# print(lc_771.numJewelsInStones(jewels, jewels, stones))


''' Leetcode 1365 How Many Numbers Are Smaller Than the Current Number?'''

# array = [8,1,2,2,3]
# # array.insert()
# print(lc_1365.smallerNumbersThanCurrent(array,array))


array = [12,334,44,5,6663,223,21,3,23,44,123,55,22,23]
print(BubbleSort.sort(array))


# array = [12,334,44,5,6663,223,21]

# array.sort()

# array = [5, 12,21,44,223,334,6663]
# # print(BinarySearch.binarySearch(array,21))

# for i in array:
#     print(i.__str__() + " is in " + BinarySearch.binarySearch(array,i).__str__())