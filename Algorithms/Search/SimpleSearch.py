import timeit

def simpleSearch(arr: list[int], target: str) -> bool: #comapre two items side by side
    for i in arr:
        if i == target:
            return arr.index(i)
    return -1

def main():
    start = timeit.default_timer()
    print(simpleSearch([1,2,3,4], 2))

    try:
        assert(simpleSearch([1,2,3,4], 2)) == 1
        assert(simpleSearch([-1,2,3,4], -1)) == 0 #it makes logical sesne that assert 
    except AssertionError:
        print('you done goofed')
    print((timeit.default_timer() - start))
    
if '__init__' == main():
    main()