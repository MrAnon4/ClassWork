
def ternary_search(arr, low, high, target, count):

        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if (count > len(arr)):
           return -1

        if (target == arr[mid1] ):
            return mid1
        elif (target == arr[mid2] ):
            return mid2

        if (target > arr[mid1]):
            return ternary_search(arr, 0, mid1-1, target, count +1 )
        elif (target < arr[mid2] ):
            return ternary_search(arr, mid2+1, len(arr)-1, target, count +1)
        elif (target < arr[mid1] and target > arr[mid2] ):
            return ternary_search(arr, mid1, mid2, target, count +1)




array1 = [443, 339, 333, 231, 202, 17, 11, 9, 8, 7, 6, 5, 4, 1]
target1 = 111
count1 = 0

print(ternary_search(array1, 0, len(array1)-1, target1, count1 ))


