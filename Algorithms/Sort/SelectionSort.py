
def selectionsort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    def isSmallest(arr: list[int]) -> int:
        smallest = arr[0]
        
        for i in arr:
            if i < smallest:
                smallest = i
        return smallest
        
    output = []
    
    while len(arr) != 0:
        small = isSmallest(arr)
        output.append(small)
        arr.remove(small)
    
    return output
        
print(selectionsort([1,4,2]))
print(selectionsort([]))
print(selectionsort([1]))
print(selectionsort([2,3]))
print(selectionsort([1,4,2,9,1]))