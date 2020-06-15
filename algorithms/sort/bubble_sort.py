def bubble_sort(arr):
    """
    Bubble sort iterates through a list, comparing neighbors and swapping them if they're not in order
    Time complexity: O(n^2)
        O(n) for already-sorted list
    Space complexity: O(1)
    This algorithm is not widely used because its time complexity is much greater than most other sorting algorithms
    """
    swaps = 1
    while swaps > 0:
        swaps = 0
        i = 0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swaps += 1
            i += 1
    
    return arr

a = [5,1,4,2,8]
print(bubble_sort(a))