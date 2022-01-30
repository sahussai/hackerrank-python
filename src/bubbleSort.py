class BubbleSort:
    @classmethod
    def sort(self, arr):
        length = len(arr)
        for i in range(0, length):
            for j in range(0, length-1-i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        
        return arr