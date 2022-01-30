class BinarySearch:
    @classmethod
    def binarySearch(cls,arr: list[int], target):
        return cls.__binarySearchHelper(arr, 0, len(arr) - 1, target)

    @classmethod
    def __binarySearchHelper(cls,sub_array: list[int], low: int, high: int, target: int):        
        middleIndex = (low + high) // 2

        if sub_array[middleIndex] == target:
            return middleIndex
        elif sub_array[middleIndex] < target:
            return cls.__binarySearchHelper(sub_array, middleIndex + 1, high,target)
        else:
            return cls.__binarySearchHelper(sub_array, low, middleIndex -1, target)



