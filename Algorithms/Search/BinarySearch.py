import timeit
from typing import Optional

#O(log n) with loge base 2 since 2^(log n) steps are required at the worst case

def binarySearch(nums: int, target: int) -> int: 
    low, high = 0, len(nums)
    
    while low <= high:
        mid = (low + high) // 2 #Returns floor of the devision
        
        if target < nums[mid]:
            high = mid - 1 #we will check left half of the list
        
        elif target > nums[mid]:
            low = mid + 1 #we will check right half of the list
        
        elif target == nums[mid]:
            return mid
    
    return -1

def main():
    start = timeit.default_timer()
    print(binarySearch([1,2,3,4], 2))

    try:
        assert(binarySearch([1,2,3,4], 2)) == 1
        assert(binarySearch([-1,2,3,4], -1)) == 0 #it makes logical sesne that assert 
    except AssertionError:
        print('you done goofed')
    print((timeit.default_timer() - start))
    
if '__init__' == main():
    main()