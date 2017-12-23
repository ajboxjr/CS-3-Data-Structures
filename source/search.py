#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if len(array)-1 >= index:
        if item == array[index]:
            return index
        else:
            index +=1
            return linear_search_recursive(array, item, index)
    else:
        return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # 1 sort items
    #while the array is greater than 0
    # get the middle value
    # check larger or smaller
    #split on that point
    array = sorted(array)
    low = 0
    high = len(array)-1
    mid = 0
    while low <= high:
        mid = int((low+high)/ 2)
        if array[mid] < item:
            low = mid +1
        elif array[mid] > item:
            high = mid -1
        else:
            print("{} found at {}".format(array[mid], mid))
            return mid
    print("Error: {} not found".format(item))
    return None


    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    #Setting Initial Values
    if left == None or right == None:
        left = 0
        right = len(array)-1

    # Get mid and remove decimal points
    mid = int((left+right)/2)
    if left <= right:
        if array[mid] == item:
            print("Item {} found {}".format(array[mid], mid))
            return mid
        elif array[mid] < item:
            return binary_search_recursive(array,item, mid+1, right)
        elif item < array[mid]:
            return binary_search_recursive(array,item, left, mid-1)
    else:
        print("Item {} not found".format(item))
        return None

if __name__ == '__main__':
    names = ["Alex","Brian","Julia","Kojin","Nabil","Nick","Winnie","Sue"]
    print(binary_search(names,"Nick"))
