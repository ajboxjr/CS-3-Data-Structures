#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: Best: 0(1) Worst: Ω(N) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    x = 0
    for x in range(len(items)-1): #O(N)
    # while x< len(items)-1:
        if items[x] > items[x+1]: #0(1)
            print(x)
            print(items[x])
            return False
        x+=1
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time:
    Best: Ω(N) sorted, worst: O(N^2) sorted reversly
    TODO: Memory usage:
    Best & Worst: 0(1) store temporary variable"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    while is_sorted(items) is False:
        index = 0
        while index < len(items)-1:
            current = items[index]
            next_elem = items[index+1]
            if current > next_elem:
                items[index] = next_elem
                items[index+1] = current
            index+=1
        print('after swap {}'.format(items))


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time:
    Best: Ω(N^2) Worst: 0(N^2) ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    # while is_sorted(items) is False:
    for start in range(len(items)):
        min_idx = start
        for index in range(start+1,len(items)):
            if items[min_idx] > items[index]:
                print("larger {} smaller {}".format(items[index], items[min_idx]))
                min_idx = index
        # print("{} the smallest ".format(min_idx))
        print("swap idx{}: {} with idx{}: {}".format(start, items[start], min_idx, items[min_idx]))
        temp_elem = items[start]
        items[start] = items[min_idx]
        items[min_idx] = temp_elem
        print("swapped idx{}: {} with idx{}: {}".format(start, items[start], min_idx, items[min_idx]))

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for idx in range(len(items)-1):
        if items[idx] > items[idx+1]:
            print("{} larger than {}".format(items[idx],items[idx+1]))
            for rev_idx in reversed(range(idx+1)): #5,4,3,2,1
                # print(rev_idx,rev_idx+1)
                # print(items[rev_idx], items[rev_idx+1])
                if items[rev_idx+1] < items[rev_idx]: #swap
                    temp_elem = items[rev_idx]
                    items[rev_idx] = items[rev_idx+1]
                    items[rev_idx+1] = temp_elem
                    print(items)
                else:
                    pass
        elif items[idx] > items[idx+1]:
            print("{} smaller than {}".format(items[idx],items[idx+1]))
    # items = insertion_sort(items)
    print(items)


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    print(items)
    while is_sorted(items) == False:
        left, right = split_items(items)
        merge(left,right)

def split_items(items):
    length = int(len(items)/2)
    return ( items[:length],items[length:])

def merge(left, right):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    print("start {}, {}".format(left,right))
    left_len = len(left)
    right_len = len(right)
    idx_l = 0
    idx_r = 0
    arr = []
    while idx_l < left_len and idx_r < right_len:
        if left[idx_l] > right[idx_r]:
            arr.append(right[idx_r])
            idx_r +=1
        elif left[idx_l] < right[idx_r]:
            arr.append(left[idx_l])
            idx_l +=1
        else:
            arr.append(left[idx_l])
            idx_l +=1

    if idx_l == left_len:
        arr.extend(right[idx_r:])
    if idx_r == right_len:
        arr.extend(left[idx_l:])
    print("end {}".format(arr))
    return arr

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    left, right = split_items(items)
    print('left: {}right: {}'.format(left,right))
    if len(left) == 1:
        sorted_arr = []
        if len(right) ==1:
            return merge(left,right)
        else:
            return merge(left,merge_sort(right))
    else:
        return merge(merge_sort(left), merge_sort(right))




def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    items =sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
